import os
import logging

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

base_path = os.environ.get('OPENAI_API_BASE', 'http://127.0.0.1:8080/v1')
key = os.environ.get('OPENAI_API_KEY', '-')
model_name = os.environ.get('MODEL_NAME', 'gpt-3.5-turbo')

llm = ChatOpenAI()

print (llm.invoke("how can langsmith help with testing?"))


