from langchain_ollama import ChatOllama
def create_candidate_model(model_name):
    if not model_name or not model_name.strip():
        raise ValueError("The model name cannot be empty.")
    else:
        llm = ChatOllama(model=model_name,temperature=0)
        return llm