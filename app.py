from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

def main():
    load_dotenv()
    st.set_page_config(page_title="Ask Your PDF")

    # Upload the file using streamlit
    pdf = st.file_uploader("Upload a PDF Here", type="pdf")

    # Checking if the PDF is present/not null, if so we will read it and extract text
    if pdf is not None:
        pdf_reader = PdfReader(pdf)

        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        # Split into chunks
        text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
        chunks = text_splitter.split_text(text)
        
        # Create embeddings and knowledge base
        embeddings = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embeddings)

        # Show user input 
        user_question = st.text_input("Enter a question about your PDF")

        # Keep asking the question until there is an input
        if user_question: 
            docs = knowledge_base.similarity_search(user_question)
            
            # Set up the QA chain and get response
            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=user_question)
                print(cb)  # For debugging purposes
            
            st.write(response)

if __name__ == '__main__':
    main()
