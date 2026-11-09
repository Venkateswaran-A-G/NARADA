from src.retrieval.vector_db import create_memory
encoder,client = create_memory()
collections = client.get_collections()
print("Collections: ")
for i in collections:
    print(i,end=" ")
collection = client.get_collection("narada_docs")
print(collection)
dimension = encoder.get_embedding_dimension()
print(f"Embedding dimension: {dimension}")