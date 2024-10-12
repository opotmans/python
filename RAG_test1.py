#ceci est un test pour implémenter un système de RAG
from llama_index.core import SimpleDirectoryReader
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter
documents = SimpleDirectoryReader("/root/data").load_data()
