from src.agent.model_factory import create_candidate_model
from src.agent.state import State



def ask_llm(state:State):
    model_name = state.get("model_name","llama3.2:latest")
    llm = create_candidate_model(model_name)
    response = llm.invoke(state["question"])
    return {"answer":response.content,"model_name":model_name}