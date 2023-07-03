from logging import Logger

import arrow
from fastapi import APIRouter
from fastapi import Request

from api.model.llm import ChatGLMRequest, QA, ChatGLMResponse
from utilities.token_helper import calc_tokens

router = APIRouter(prefix="/api/llm", tags=["LLM"])


@router.post("/chat", summary="Chat with ChatGLM model.", response_model=ChatGLMResponse)
async def send_chat_request(req: Request, chat_request: ChatGLMRequest):
    logger: Logger = req.app.state.logger
    history_messages = None
    if chat_request.history:
        history_messages = [[msg.question, msg.answer] for msg in chat_request.history]

    start = arrow.utcnow()

    response, history = req.app.state.llm.chat(
        req.app.state.tokenizer,
        chat_request.prompt,
        history=history_messages,
        max_length=chat_request.max_length if chat_request.max_length else 2048,
        top_p=chat_request.top_p if chat_request.top_p else 0.7,
        temperature=chat_request.temperature if chat_request.temperature else 0.95)
    # print(json.dumps(chat_request.dict(), indent=4))

    prompt_token = 0
    response_token = 0
    now = arrow.utcnow()

    if chat_request.prompt:
        prompt_token = calc_tokens(chat_request.prompt)
    history_messages = []
    if history and chat_request.with_history:
        history_messages = [QA(question=qa[0], answer=qa[1])for qa in history]
        prompt_token += sum((calc_tokens(qa)for qa in history))

    response_token = calc_tokens(response)
    resp = ChatGLMResponse(
        response=response,
        history=history_messages,
        start=start.isoformat(),
        end=now.isoformat(),
        took=(now-start).total_seconds(),
        prompt_token=prompt_token,
        response_token=response_token,
        total_token=prompt_token + response_token
    )

    logger.debug(f"Prompt: {chat_request.prompt} Response: {response}")
    # torch_gc()
    return resp


