import os
from crewai import Agent, Task, Crew, Process

#from langchain_openai import ChatOpenAI 
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "sk-1111"

llm_lmstudio = OpenAI(base_url="http://127.0.0.1:11434/v1",api_key="")

#Create researcher agent 
researcher = Agent (
    role = "Expert Research",
    goal = " Discover 2024 Technologies Trends",
    backstory =" After 20 years in the technology world, I would like to maintain the level of my knowledge on the top to stay in the small group of experts  ",
    verbose = True,
    llm=llm_lmstudio
)

#Create a writer agent
writer = Agent ( 
    role = "Writer",
    goal = "Create a summary of the different technologies trends",
    verbose = True,
    backstory = "a creative writer who is able to translate the techies content into a readable content understanble by common people",
    llm=llm_lmstudio
)

#Task for the researcher

research_task = Task (
    description = "identify the new most important trends coming in 2024",
    agent = researcher
)

writer_task = Task (
    description = "write a blog post that summarizes a list of 5 trends coming in 2024",
    agent = writer
)

Tech_crew = Crew (
    agents = [researcher, writer],
    tasks = [research_task, writer_task],
    process = Process.sequential 
)

result = Tech_crew.kickoff()

print ("################################")
print (result)



