from crewai import Agent, Task, LLM, Crew
from crewai.process import Process
from crewai_tools import ScrapeWebsiteTool, SerperDevTool,SeleniumScrapingTool

Ollama_llm =LLM (
		model ='ollama/llama3.2:latest',
		timeout =120,
		num_ctx = 20000,
		base_url="http://localhost:11434",
		max_tokens = 10000
	)

Website_Search_Agent = Agent(
    role="Search the web sites",
    goal="Find the most relevant web sites about a specific {topic}",
    backstory=" You are an expert who is able to find the best web sites",
    max_iter = 3,
    tool = [SerperDevTool()],
    llm = Ollama_llm,
    max_execution_time = 30,
    verbose = True,
    max_retry_limit = 0,
)

Scrap_Agent = Agent(
    role ="Scrap Agent",
    goal ="Scrape a website based on the {url}",
    backstory="you are an expert that scrap website to find the most relevant information",
    max_iter =1,
    verbose = True,
    max_retry_limit=0,
    llm=Ollama_llm,
    tool = [SeleniumScrapingTool()]
)

scrap_task = Task(
    description = """This task consists of the extraction of the most relevant information related to the company
    """,
    expected_output = "the vision, the strategy and the directors of the company, if you don't find the information about a specific theme, don't propose something that's not relevant. Try to capture information in the blog post by completings the url with /blog", 
    agent = Scrap_Agent
)

website_search_task = Task(
    description ="""Select the best and most relevant websites about a specific {topic}. There is no space in the url, no underscore
    Make sure that this site is interesting and give elements helping to create a wonderful summary.
    Try to capture information about sustanaibility in the blog section that you can access using /blog.
    """,
    expected_output="""The list of the selected web sites
    """,
    output_file ="report.md",
    agent = Scrap_Agent
)


crew = Crew (
    agents=[Scrap_Agent],
    tasks =[scrap_task],
    process = Process.sequential,
    verbose = True
)

result = crew.kickoff(inputs ={'url' : 'https://www.ngageconsulting.com'} )

