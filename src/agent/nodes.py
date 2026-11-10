from langchain_ollama import ChatOllama
from src.agent.state import State

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

def ask_llm(state:State):
    response = llm.invoke(state["question"])
    return {"answer":response.content}