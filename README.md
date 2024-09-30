# ollama_chatbot
This is an simple ai chat bot with different llm (you can choose it)
---
# Setup

## To install ollama in linux
```
curl -fsSL https://ollama.com/install.sh | sh
```

## Run the ollama locally
```
ollama serve 
```

## Open a new terminal

## run this command to pull a model

```
ollama pull llama3.2
```

## now to run the model use
```
ollama run llama3.2
```

### And then type your question and youll get response and ctrl+d to exit

## Or with queestion directly

```
ollama run llama3.2 "what is AI in short"
```

## to remove a model run 
```
rm -rf ~/.ollama/models/manifests/registry.ollama.ai/library/llama3.2
```
## here llama3.2 is model name it should be changed which model you want delete
## To list all the models pulled run 

```
ls ~/.ollama/models/manifests/registry.ollama.ai/library
```

## To run flask app
```
python app.py
```