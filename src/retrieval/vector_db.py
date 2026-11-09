from qdrant_client import models,QdrantClient
from sentence_transformers import SentenceTransformer
def create_memory():
    encoder = SentenceTransformer("all-MiniLM-L6-v2")
    client = QdrantClient(":memory:")
    client.create_collection(
        collection_name="narada_docs",
        vectors_config=models.VectorParams(
            size=encoder.get_embedding_dimension(),
            distance=models.Distance.COSINE,
        ),
    )
    return encoder,client

