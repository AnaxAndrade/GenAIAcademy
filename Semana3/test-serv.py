from langchain_ollama import ChatOllama

def main():
    llm = ChatOllama(base_url="http://lab.entercoding.com:11434", model="gemma3:27b")
    
    question = "What is the capital of France?"
    response = llm.invoke(question)
    print(response.content)

if __name__ == "__main__":
    main()
