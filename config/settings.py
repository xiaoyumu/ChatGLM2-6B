from pydantic import BaseSettings


class Settings(BaseSettings):
    api_name: str = "ChatGLM2-6B API"
    api_version: str = "0.0.1"
    host: str = "0.0.0.0"  # "0.0.0.0"
    port: int = 8081
    debug: bool = True
    prefix: str = ""
    openapi_prefix: str = ""
    timeout_keep_alive: int = 120
    log_level: str = "debug"

    llm_model_v2: str = "E:\\ai\\nlp\\llm\\THUDM\\chatglm2-6b"
    chat_glm_model_version: str = "2"
    torch_hub_dir: str = "E:\\ai\\nlp\\torch"
    huggingface_home_dir: str = "E:\\ai\\huggingface_cache"



