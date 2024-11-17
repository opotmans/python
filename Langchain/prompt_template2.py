from langchain_ollama.llms import OllamaLLM

llm = OllamaLLM(
     model="llama3.2",
     temperature=0.7,
     num_predict = 256,
     )

#----------------------------------------------------------------------
#Use of PromptTemplate
#----------------------

from langchain_core.prompts import PromptTemplate,check_valid_template

#Exercice 1 : utlisation de la fonction from_template de PromptTemplate
#=======================================================================

# template = """ Could you please givem a {topic} about {action}"""

# prompt = PromptTemplate.from_template(
#     partial_variables = {'topic':'joke','action':'cat'},
#     template = template,
# )

# #display the prompt when variables are used in html or normal text
# print (prompt.pretty_repr())
# print (prompt.pretty_print())


# result = prompt | llm

# print(result.invoke(prompt.partial_variables))


#Exercice 2 : Save the prompt
#=============================

# template = """ Give me the 10 first numbers of Pi"""
# prompt = PromptTemplate.from_template(
#     template = template,
# )

# prompt.save("/home/opotmans/Langchain/prompt_save.yaml")

# result = prompt | llm

# print(result.invoke(prompt.partial_variables))

#Exercice 3: Load a prompt
#==========================

# prompt = PromptTemplate.from_file (
#     template_file = "/home/opotmans/Langchain/prompt.txt",
# )

# result = prompt | llm 
# print (result.invoke(prompt.partial_variables))
# check_valid_template (prompt)

# -----------------------------------------------------------------------------
#ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate,check_valid_template 

#Exercice 1: ChatpromptTemplate 
#==============================

# prompt = ChatPromptTemplate([
#     ("system","you are a specialist in {techno}"),
#     ("human","Could you please define microsoft entra"),
#     ("AI","")
# ])

# from langchain_core.output_parsers import StrOutputParser

# analysis_prompt = ChatPromptTemplate.from_template("is this a funny joke? {joke}")

# composed_chain = {"joke": chain} | analysis_prompt | llm | StrOutputParser()

# composed_chain.invoke({"topic": "bears"})

#Exercice 2 : JsonOutputParser
# ============================
# Define your desired data structure.

from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")
    conclusion : str = Field (description="explain the joke")

# And a query intented to prompt a language model to populate the data structure.
joke_query = "Tell me a joke."

# Set up a parser + inject instructions into the prompt template.
output_parser = JsonOutputParser(pydantic_object=Joke)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)

chain = prompt | llm | output_parser

result=chain.invoke({"query": joke_query})

print(result) 

#Exercice 3 : JsonOutputParser
# ============================
# Define your desired data structure.
# from langchain_core.output_parsers import CommaSeparatedListOutputParser

# output_parser = CommaSeparatedListOutputParser()
# format_instructions = output_parser.get_format_instructions()
# prompt = PromptTemplate(
#     template="Who is {subject}.\n{format_instructions}",
#     input_variables=["subject"],
#     partial_variables={"format_instructions": format_instructions},
# )
# chain = prompt | llm | output_parser

# result=chain.invoke({"subject": "Einstein"})

# print(result)

