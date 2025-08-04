import os
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
from langchain_openai import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

load_dotenv()
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fa;
        font-family: 'Helvetica Neue', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

image = Image.open("banner.png")
image_resized = image.resize((1200,600))
st.image(image_resized)
st.header("News Research Tool")

st.sidebar.markdown("### 🔗 Enter News URLs")
faiss_index_path = "faiss_store_openai"

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")


URLs=[]
for i in range(3):
   url= st.sidebar.text_input(f"URL {i+1}")
   URLs.append(url)

process_url_clicked =st.sidebar.button("Process URLs")
main_placefolder = st.empty()
llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0.7)
print("LLM Model being used:",llm.model_name)

if process_url_clicked:
    #load 

    loader=UnstructuredURLLoader(urls=URLs)
    main_placefolder.text("Data Loading Started...")
    data =loader.load()
    
    #Splitting the data
    splitter =RecursiveCharacterTextSplitter(separators=["\n\n","\n",".",","],chunk_size=1000)
    main_placefolder.text("Data Splitting Started...")
    docs = splitter.split_documents(data)

    #create embeddings
    vectorstore_openai=FAISS.from_documents(docs,embeddings)
    main_placefolder.text("Embedding Vector Started Building..")


    vectorstore_openai.save_local(faiss_index_path)
    main_placefolder.text("FAISS Index Saved Successfully ✅")

query = main_placefolder.text_input("Question:")

if query:
    if os.path.exists(faiss_index_path):
        vectorstore = FAISS.load_local(faiss_index_path, embeddings,allow_dangerous_deserialization=True)
        chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
        result = chain.invoke({"question":query})

        st.header("Answer")
        st.subheader(result["answer"])
   
        sources = result.get("sources", "")
        if sources:
            st.write("Sources:")
            for source in sources.split("\n"):
                st.write(f"- {source}")
        else:
            st.write("No sources returned by the model.")
    else:
      st.error("FAISS index not found, please process URLs first.")
