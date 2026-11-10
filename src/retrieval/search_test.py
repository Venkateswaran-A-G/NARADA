from qdrant_client.models import PointStruct
from src.retrieval.vector_db import create_memory
from pathlib import Path
encoder,client = create_memory()
p = Path('data/docs/sample.txt')
lines = p.read_text().splitlines()

embedding= encoder.encode(lines)
print("Number of Lines: ",embedding.shape[0])
print("Vector Size: ",embedding.shape[1])

for i,line in enumerate(lines):
    client.upsert(
    collection_name="narada_docs",
    points=[
        PointStruct(
            id = i,
            vector=embedding[i].tolist(),
            payload={
                "text":line
            }
        )
    ]
)
collection = client.get_collection("narada_docs")
print("Points Count: ",collection.points_count)

question = "Which tool stores vectors and finds similar information?"
query = encoder.encode(question).tolist()
result = client.query_points(
    collection_name="narada_docs",
    query=query,
    limit=1,
    with_payload=True
)
point = result.points[0]
print("Text:", point.payload["text"])
print("Score:", point.score)