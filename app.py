from dotenv import load_dotenv
# import os
import streamlit as st
from PyPDF2 import PdfReader;

from langchain.text_splitter import CharacterTextSplitter

def main():
    load_dotenv();
    # print(os.getenv("OPENAI_API_KEY"))
    st.set_page_config(page_title="Ask Your PDF")

    
    # Upload the file using streamlit
    pdf = st.file_uploader("Upload a PDF Here", type="pdf")

    # Checking if the PDF is present/not null, if so we will read it and extract text
    if pdf is not None:
        pdf_reader = PdfReader(pdf);

        text=""
        for page in pdf_reader.pages:
            text+= page.extract_text();

        # Split into chunks

        text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200,length_function=len)

        chunks = text_splitter.split_text(text);

        st.write(chunks)


if __name__ == '__main__':
    main()