from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from crewai.process import Process

Ollama_llm =LLM (
		model ='ollama/deepseek-r1',
		timeout =120,
		num_ctx = 20000,
		base_url="http://localhost:11434",
		max_tokens = 10000,
        temperature = 1
	)

Web_Search_Agent = Agent(
    role = "Senior Web Search",
    goal = "Find all information about a specific {topic}",
    backstory = " You are an expert that are able to find the right and interesting web site about a specific {topic}",
    allow_delegation = False,
    llm = Ollama_llm,
    tool =[SerperDevTool()],
    verbose = True
    )


Scraper_Agent = Agent(
    role = "Senior Scraper Website",
    goal = "Scrap the page based on the urls identified by the Web_Search_Agent",
    backstory =" you are an expert to scrap the website to extract the relevant information related to the specific {topic}", 
    max_iter = 1,
    max_retry_limit = 1, 
    tool = [ScrapeWebsiteTool()],
    llm = Ollama_llm,
    verbose = True
    )

Research_Agent = Agent(
    role = "Senior Data Scientist",
    goal = "Find and summarize information about a specific {topic}",
    backstory ="You are an expert in data analysis with attention to all the details",
    max_iter = 5,
    allow_delegation = False,
    llm = Ollama_llm,
    verbose = True
    )

Web_Search_task = Task(
 description="""
        Search the most relevant website related to the specific {topic}
        Make sure you find any interesting and relevant information given
        the current year is 2024.
    """,
    expected_output="""
        A list of web sites relevant about {topic}
    """,
    output_file = "Search.md",
    agent=Web_Search_Agent
)

Scraper_Task = Task(
     description="""
        Scrap the website related based on the url given by the Web_search_Agent.
        Make sure you find any interesting and relevant information given
        the current year is 2024.
    """,
    expected_output="""
        A list with 10 bullet points of the most relevant information about {topic}
    """,
    context = [Web_Search_task],
    output_file = "Scraper.md",
    agent=Scraper_Agent
)

Research_task = Task (
    description="""
        Conduct a thorough research about {topic}.
        Make sure you find any interesting and relevant information given
        the current year is 2024.
    """,
    expected_output="""
        A list with 10 bullet points of the most relevant information about {topic}
    """,
    output_file = "report.md",
    agent=Research_Agent
)


crew = Crew(
    agents=[Web_Search_Agent,Scraper_Agent,Research_Agent],
    tasks=[Web_Search_task,Scraper_Task,Research_task],
    process=Process.sequential,
    verbose=True
)

crew_output = crew.kickoff(inputs={'topic':"ngageconsulting"})

print(f"Tasks Output: {crew_output.tasks_output}")
print(f"Token Usage: {crew_output.token_usage}")