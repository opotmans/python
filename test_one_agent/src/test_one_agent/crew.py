from crewai import Agent, Crew, Process, Task,LLM
from crewai.project import CrewBase, agent, crew, task, before_kickoff, after_kickoff

# Uncomment the following line to use an example of a custom tool
# from test_one_agent.tools.custom_tool import MyCustomTool

# Check our tools documentations for more information on how to use them
# from crewai_tools import SerperDevTool

@CrewBase
class TestOneAgent():
	"""TestOneAgent crew"""

	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	ollama_llm =LLM (
		model ='ollama/deepseek-r1',
		timeout =120,
		num_ctx = 20000,
		base_url="http://localhost:11434",
		max_tokens = 10000
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
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			max_iter=1,
			# tools=[MyCustomTool()], # Example of custom tool, loaded on the beginning of file
			verbose=True,
			llm = self.ollama_llm
		)

	@agent
	def reporter(self) -> Agent:
	 	return Agent(
	 		config=self.agents_config['reporter'],
			max_iter=1,
			verbose=True,
			llm = self.ollama_llm
	 	)

	@task
	def write_task(self) -> Task:
		return Task(
			config=self.tasks_config['write_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the TestOneAgent crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
