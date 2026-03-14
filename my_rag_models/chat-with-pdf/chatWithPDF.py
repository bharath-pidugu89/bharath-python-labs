import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_classic.chains import RetrievalQA

# 1. SETUP: Setting API Key
os.environ["OPENAI_API_KEY"]

def build_rag_system(file_path):
    # 2. LOAD: Extract text from PDF
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    # 3. SPLIT: Break text into chunks
    # using overlap so context isn't lost at the edges of a cut - Sliding window
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, 
        chunk_overlap=200
    )
    chunks = text_splitter.split_documents(documents)

    # 4. EMBED & STORE: Convert text to numbers and save in ChromaDB
    # 'persist_directory' saves the data to your hard drive
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=OpenAIEmbeddings(),
        persist_directory="./chroma_db"
    )

    # 5. RETRIEVAL & GENERATION: Create the "Chain"
    llm = ChatOpenAI(model_name="gpt-4o", temperature=0)
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff", # "Stuffing" all retrieved chunks into one prompt
        retriever=vector_db.as_retriever()
    )
    
    return rag_chain

# --- Execution ---
my_rag = build_rag_system(r"C:\Users\Bharath\AI-ML\bharath-python-labs\my_rag_models\chat-with-pdf\Chapter1.pdf")
query = "What are the main conclusions of this document?"
response = my_rag.invoke(query)

print(f"AI Response: {response['result']}")