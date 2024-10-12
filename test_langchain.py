from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


prompt = ChatPromptTemplate.from_messages([
    ("user", "{input}")
])

llm = Ollama(model="dolphin-mistral:latest")

output_parser = StrOutputParser()

chain = prompt | llm | output_parser

print (chain.invoke({"input": "who is Einstein"}))
