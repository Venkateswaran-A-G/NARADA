from langchain_ollama import ChatOllama
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)
message = [("system","You are a helpful AI assistant"),("human","What is the capital of France?"),]
ai_msg = llm.invoke(message)
print(ai_msg.content_blocks)