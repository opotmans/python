#from llama_index.llms.ollama import Ollama xxx
from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter
documents = SimpleDirectoryReader("/root/data").load_data()
print(documents)