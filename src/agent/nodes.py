from src.agent.model_factory import create_candidate_model
from src.agent.state import State
from src.retrieval.retriever import retrieve_text

def ask_llm(state:State):
    question = state["question"]
    model_name = state.get("model_name","llama3.2:latest")
    use_retrieval = state.get("use_retrieval", False)
    document_path = state.get("document_path", None)
    model_input = question
    if use_retrieval:
        retrieved_text = retrieve_text(question, document_path=document_path)
        if not retrieved_text or not retrieved_text.strip():
            raise ValueError("No text was retrieved from the document. This is a retrieval failure, not a model answer.")
        
        model_input = (
            f"Use only the following context to answer the question. "
            f"If the answer is not contained in the context, state that you cannot find the answer.\n\n"
            f"Context:\n{retrieved_text}\n\n"
            f"Question: {question}"
        )


    llm = create_candidate_model(model_name)
    response = llm.invoke(model_input)
    return {"answer":response.content,"model_name":model_name}