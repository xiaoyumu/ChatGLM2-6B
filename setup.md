## How To Setup



```commandline
# Install pytorch with conda and CUDA support first
$ conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia

# Then
$ pip install -r requirements_default.txt

```


Models

```
mkdir E:\ai\nlp\llm\THUDM

# V1 Models
git clone https://huggingface.co/THUDM/chatglm-6b

# V2 Models
git clone https://huggingface.co/THUDM/chatglm2-6b

```