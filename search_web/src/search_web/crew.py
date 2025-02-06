from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff
from crewai_tools import SerperDevTool,ScrapeWebsiteTool,FileWriterTool
from dotenv import load_dotenv

# Uncomment the following line to use an example of a custom tool
# from search_web.tools.custom_tool import MyCustomTool
load_dotenv()

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class SearchWeb():
	"""SearchWeb crew"""
	
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	ollama_llm =LLM (
		model ='ollama/deepseek-r1',
		timeout =120,
		num_ctx = 20000,
		base_url="http://localhost:11434",
		max_tokens = 10000,
		temperature = 1
	)

	@before_kickoff # Optional hook to be executed before the crew starts
	def pull_data_example(self, inputs):
		# Example of pulling data from an external API, dynamically changing the inputs
		inputs['extra_data'] = "This is extra data"
		return inputs

	@after_kickoff # Optional hook to be executed after the crew has finished
	def log_results(self, output):
		# Example of logging results, dynamically changing the output
		print(f"Results: {output}")
		return output

	@agent
	def retrieve_news(self) -> Agent:
		return Agent(
			config=self.agents_config['retrieve_news'],
			tools=[SerperDevTool()], # Use this tool to ask to google to retrieve news about a specific topic
			verbose=True,
			llm = self.ollama_llm
		)

	@agent
	def website_scraper(self) -> Agent:
		return Agent(
			config=self.agents_config['website_scraper'],
			tools =[ScrapeWebsiteTool()],
			verbose=True,
			llm = self.ollama_llm
		)

	@agent
	def ai_news_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['ai_news_writer'],
			tools =[],
			verbose=True,
			llm = self.ollama_llm
		)

	@agent
	def file_writer(self) -> Agent:
		return Agent(
			config=self.agents_config['file_writer'],
			tools =[FileWriterTool()],
			verbose=True,
			llm = self.ollama_llm
		)

	@task
	def retrieve_news_task(self) -> Task:
		return Task(
			config=self.tasks_config['retrieve_news_task'],
		)

	@task
	def website_scrape_task(self) -> Task:
		return Task(
			config=self.tasks_config['website_scrape_task'],
		)

	@task
	def ai_news_write_task(self) -> Task:
		return Task(
			config=self.tasks_config['ai_news_write_task'],
		)

	@task
	def file_write_task(self) -> Task:
		return Task(
			config=self.tasks_config['file_write_task'],
		)


	@crew
	def crew(self) -> Crew:
		"""Creates the SearchWeb crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			# memory=True,
		    verbose=True,
			# embedder={
			# 	"provider": 'ollama',
			# 	"config": {
			# 		"model":"llama3.2" 
			# }
			#} 
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
