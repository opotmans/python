from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
#
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama

documents = SimpleDirectoryReader("/root/data").load_data()

# bge-base embedding model
Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")

# ollama
Settings.llm = Ollama(model="dolphin-mistral:latest", request_timeout=360.0)

index = VectorStoreIndex.from_documents(
    documents,
)

query_engine = index.as_query_engine()
response = query_engine.query("what are the pillars of the platform engineering ? ")
print(response)