from dotenv import load_dotenv
# import os
import streamlit as st

def main():
    load_dotenv();
    # print(os.getenv("OPENAI_API_KEY"))
    st.set_page_config(page_title="Ask Your PDF")


if __name__ == '__main__':
    main()