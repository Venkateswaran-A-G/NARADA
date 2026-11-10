from qdrant_client.models import PointStruct
from src.retrieval.vector_db import create_memory
from pathlib import Path
encoder,client = create_memory()
p = Path('data/docs/sample.txt')
lines = p.read_text().splitlines()

embedding= encoder.encode(lines)
print("Number of Lines: ",embedding.shape[0])
print("Vector Size: ",embedding.shape[1])

client.upsert(
    collection_name="narada_docs",
    points=[
        PointStruct(
            id = 1,
            vector=embedding[0].tolist(),
            payload={
                "text":lines[0]
            }
        )
    ]
)
collection = client.get_collection("narada_docs")
print("Points Count: ",collection.points_count)