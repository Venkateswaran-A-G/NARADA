from typing_extensions import TypedDict
from langgraph.graph import START,END,StateGraph
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)
class State(TypedDict):
    question:str
    answer:str
def ask_llm(state:State):
    response = llm.invoke(state["question"])
    return {"answer":response.content}
graph = (
    StateGraph(State)
    .add_node("ask_llm",ask_llm)
    .add_edge(START,"ask_llm")
    .add_edge("ask_llm",END)
    .compile()
)
result = graph.invoke({"question":"What is the capital of France?"})
print(result)
