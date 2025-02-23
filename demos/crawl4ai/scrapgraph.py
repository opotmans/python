from scrapegraphai.graphs import SmartScraperGraph

# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "model": "ollama/llama3.2:latest",
        "model_tokens": 20000
    },
    "verbose": True,
    "headless": False,
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="Extract useful information from the webpage, including a description of what the company does, founders and social media links",
    source="https://www.ngageconsulting.com/blog",
    config=graph_config
)

# Run the pipeline
result = smart_scraper_graph.run()

import json
print(json.dumps(result, indent=4))