from src.retrieval.vector_db import create_memory
from pathlib import Path
encoder,client = create_memory()
p = Path('data/docs/sample.txt')
embedding= encoder.encode(p.read_text().splitlines())
print("Number of Lines: ",embedding.shape[0])
print("Vector Size: ",embedding.shape[1])
