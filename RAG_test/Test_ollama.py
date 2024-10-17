from llama_index.core import SimpleDirectoryReader, StorageContext
from llama_index.core import VectorStoreIndex
#from llama_index.embeddings.fastembed import FastEmbedEmbedding
#from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.llms.ollama import Ollama

import os
os.environ ['TF_ENABLE_ONEDNN_OPTS'] = '0'
print ("test")
# Load the document for the creation of the knowledge based"
documents = SimpleDirectoryReader("/root/data").load_data()
#print(documents)

# Load the embedding model
# Option 1 : use the huggingface requires the installation of the modules
# download le modèle bert sur huggingface
#test
print("enter into Hugging")

from llama_index.embeddings.huggingface import HuggingFaceEmbedding
embed_model = HuggingFaceEmbedding()


#Indexing and storing embedding on disk
#import llama_index.vector_stores.qdrant import QdrantVectorStore
#from six import _thread

print("enter into qdrant")
from llama_index.vector_stores.qdrant import QdrantVectorStore
import qdrant_client
import qdrant_client.http.models as qmodels
from qdrant_client.http.models import *


client = qdrant_client.QdrantClient(
    host = "172.22.208.167",
    port = 6333
    )



client.recreate_collection(
        collection_name="RAG_test",
        vectors_config=qmodels.VectorParams(
            size = 384,
            distance=qmodels.Distance.COSINE
        )
)


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
