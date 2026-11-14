from qdrant_client.models import PointStruct
from src.retrieval.vector_db import create_memory
from pathlib import Path
from functools import cache


@cache
def prepare_index(path):
    encoder,client = create_memory()
    lines = [line for line in path.read_text().splitlines() if line.strip()]
    if not lines:
        return encoder, client
    embedding= encoder.encode(lines)
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
    return encoder,client

def retrieve_text(question,document_path = None):
    root = Path(__file__).resolve().parents[2]
    if document_path is None:
        chosen_path = root/"data"/"docs"/"sample.txt"
    else:
        doc_path = Path(document_path)
        if not doc_path.is_absolute():
            chosen_path = root / doc_path
        else:
            chosen_path = doc_path
    resolved_path = chosen_path.resolve()
    encoder,client = prepare_index(resolved_path)
    query = encoder.encode(question).tolist()
    result = client.query_points(
        collection_name="narada_docs",
        query=query,
        limit=1,
        with_payload=True
    )
    if not result.points:
        return ""
    else:
        point = result.points[0]
        if point.payload is None:
            return ""
        text = point.payload.get("text","")
        if text is None:
            return ""
        return text 
