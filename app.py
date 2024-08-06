from dotenv import load_dotenv
# import os
import streamlit as st
from PyPDF2 import PdfReader;

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

        st.write(text);


if __name__ == '__main__':
    main()