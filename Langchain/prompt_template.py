from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

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

chain = prompt | llm

response = chain.invoke ({
    "input": "peux-tu me donner les 10 premiers chiffres de pi"
    })
print (response)

