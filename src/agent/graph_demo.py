from src.agent.graph import build_graph
graph = build_graph()
result = graph.invoke({"question":"What is the capital of France?"})
print(result['answer'])
