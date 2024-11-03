from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from typing import Dict,Any


llm = OllamaLLM(
    model="dolphin-mistral:latest",
    temperature=0.7,
    num_predict = 256,
    )

prompt = ChatPromptTemplate.from_messages ([
    ("system", "you are a specialist in mathematics"),
    ("human", "{input}"),
]
)

prompt2 = PromptTemplate.from_template ("Tell me a joke about {topic} related to {action}")
variables:Dict[str,Any] = {"topic":"cat","action":"run"}
result = prompt2 | llm 

# result = prompt2 | llm
print (result.invoke ([{"topic":"cat"},{"action":"run"}]))
# print (result)


# chain = prompt2 | llm

# response = chain.invoke ({
#     "input": "peux-tu me donner les 10 premiers chiffres de pi"
#     })


# chain.invoke({"topic" :"cat"})
# print(chain)

# #print (response)

