from src.agent.state import State
from src.agent.nodes import ask_llm
from langgraph.graph import START,END,StateGraph

def build_graph():
    graph = (
        StateGraph(State)
        .add_node("ask_llm",ask_llm)
        .add_edge(START,"ask_llm")
        .add_edge("ask_llm",END)
        .compile()
    )
    return graph
