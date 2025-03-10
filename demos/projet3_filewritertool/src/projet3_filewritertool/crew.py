from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, before_kickoff,after_kickoff
from crewai_tools import FileWriterTool
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict
from dotenv import load_dotenv
#import agentops

#create an instance for the tools
writer = FileWriterTool()

#introduction of Pydantic classes
class ResearchUnit(BaseModel):
	finding : str = Field(...,description="A finding related to the topic")
	title : str = Field(...,description="An elegant title for this finding")
	content: str= Field(...,description="the content describe the finding in more than 20 lines")
	sources: List[Dict[str,str]]=Field(...,
		description="the different sources for this topic with title and url",
		default_factory=list
		)
class ResearchOutput(BaseModel):	
	research_list : List[ResearchUnit] = Field(...,description="list of the findings")
	summary : str = Field(...,description="A brief summary in five lines about the topic")

class ExecutiveReport(BaseModel):
	title : str = Field(...,description="title of the report")
	generation_date : str = Field(...,description="date of the generated report")
	executive_summary : str = Field(...,description="Executive summary of the analysis")
	#report_sections : List[Dict[str,str]] = Field(...,description="All sources used for the creation of this report")

load_dotenv()

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


#agentops.init("6862aa27-cf39-46eb-b4c2-b9b42ada3b1e")

@CrewBase
class Projet3Filewritertool:
	"""Projet3Filewritertool crew"""

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	ollama_llm =LLM (
		model ='ollama/llama3.2:latest',
		#timeout =120,
		base_url="http://localhost:11434",
		max_tokens = 20000,
		temperature = 0.5
	)

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			llm=self.ollama_llm,
			verbose=True
		)

	@agent
	def writer(self) -> Agent:
		return Agent(
			config=self.agents_config['writer'],
			llm=self.ollama_llm,
			verbose=True,
		)
	
	@agent
	def formater(self) -> Agent:
		return Agent(
			config=self.agents_config['formater'],
			llm=self.ollama_llm,
			verbose=True,
		)

	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
			output_pydantic = ResearchOutput,
		)
	
	@task
	def write_file_task(self) -> Task:
		return Task(
			config=self.tasks_config['write_file_task'],
			#context=[self.research_task],
			output_pydantic = ExecutiveReport,
		)
	
	@task
	def format_task(self) -> Task:
		return Task(
			config=self.tasks_config['format_task'],
			#context=[self.research_task],
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the Projet3Filewritertool crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge
		
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
#writer.run(content=ResearchOutput,filename="example.txt",overwrite="True")