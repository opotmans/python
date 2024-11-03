from langchain_ollama import OllamaLLM

llm = OllamaLLM(
    model="dolphin-mistral:latest",
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

prompt = PromptTemplate.from_file (
    template_file = "/home/opotmans/Langchain/prompt.txt",
)

result = prompt | llm 
print (result.invoke(prompt.partial_variables))
check_valid_template (prompt)
# -----------------------------------------------------------------------------
