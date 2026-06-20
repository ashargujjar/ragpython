from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
import os
loader=PyPDFLoader("./portfolio pdf updates1.pdf")
textSplitter=RecursiveCharacterTextSplitter(
  chunk_size=1000,
  chunk_overlap=200
)
api_key = os.environ.get("OPENAI_API_KEY")
chunks=loader.load_and_split(text_splitter=textSplitter)
embedings=OpenAIEmbeddings(
  api_key=api_key
  model="text-embedding-3-small"
)
vectorstore = FAISS.from_documents(
    chunks,
    embedings
)
retriever = vectorstore.as_retriever()
prompt = ChatPromptTemplate.from_template("""
Answer the question using only the context below.

Context:
{context}

Question:
{question}
""")

llm = ChatOpenAI(model="gpt-4o-mini",api_key=api_key)
# 6. Build RAG Chain (LCEL)
rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | StrOutputParser()
)
response = rag_chain.invoke(
    "tell me about ashar ashraf"
)

print(response)