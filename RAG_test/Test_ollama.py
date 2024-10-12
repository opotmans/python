from llama_index.llms.ollama import Ollama

#Initialize the model Mistral
llm = Ollama (model="dolphin-mistral:latest")
response = llm.complete ("Write a cover letter")
print (response)

