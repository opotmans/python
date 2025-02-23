from scrapegraphai.graphs import SmartScraperGraph
from langchain_core.prompts import PromptTemplate
import nest_asyncio
nest_asyncio.apply()

graph_config = {
    "llm": {
        "model": "ollama/llama3.2:latest",
    },
    "verbose": True,
    "headless": False,
}

prompt= "Extract all the List of the urls linked to blog posts"

source="https://www.ngageconsulting.com/blog"

smart_scraper_graph=SmartScraperGraph(prompt,source,graph_config)

# Run the pipeline
result = smart_scraper_graph.run()

print(result)

# import json
# print(json.dumps(result, indent=4))
