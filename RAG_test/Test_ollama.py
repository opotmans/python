from llama_index.core import SimpleDirectoryReader, StorageContext
from llama_index.core import VectorStoreIndex

#from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.llms.ollama import Ollama


# Load the document for the creation of the knowledge based"
documents = SimpleDirectoryReader("/root/data").load_data()
print(documents)

# Load the embedding model
# Option 1 : use the huggingface requires the installation of the modules
# download le modèle bert sur huggingface

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
embed_model = HuggingFaceEmbedding()

#Indexing and storing embedding on disk
#import llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.vector_Stores.qdrant import QdrantVectorStore
import qdrant_client

client = qdrant_client.QdrantClient(url="http://172.17.0.3:6333")

vector_store = QdrantVectorStore(client=client, collection_name="RAG_test")
#import chromadb
#from llama_index.vector_stores.chroma import ChromaVectorStore
#db = chromadb.PersistentClient(path="./test_chromadb")
#chroma_collection = db.get_or_create_collection("test_collection")
#vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

index= VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    embed_model = embed_model
)



#Initialize the model Mistral
#llm = Ollama (model="dolphin-mistral:latest")
#response = llm.complete ("Write a cover letter")
#print (response)
