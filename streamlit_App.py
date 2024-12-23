import os
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from phidata.agent import Agent
from phidata.model.groq import Groq


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("GROQ_API_KEY is missing. Please add it to the .env file.")

agent = Agent(
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    markdown=True
)


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def main():
    st.set_page_config(page_title="Genie RAG Application", layout="wide")

    st.markdown("""## Document Genie: Get instant insights from your Documents""")

    
    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files:", accept_multiple_files=True, key="pdf_uploader")
        if st.button("Submit & Process", key="process_button"):
            if pdf_docs:
                st.success(f"Uploaded {len(pdf_docs)} PDF(s). Processing...")
                with st.spinner("Processing PDFs..."):
                    raw_text = get_pdf_text(pdf_docs)
                    st.session_state["pdf_text"] = raw_text
                    st.success("PDFs processed and text extracted!")

    
    user_question = st.text_input("Ask a question (related to PDFs or general queries):", key="user_question")

    if user_question:
        with st.spinner("Generating response..."):
           
            pdf_context = st.session_state.get("pdf_text", "")
            if pdf_context:
                
                structured_prompt = (
                    f"Use the following context to answer the question:\n\n"
                    f"Context:\n{pdf_context}\n\n"
                    f"Question: {user_question}\n\n"
                    f"Answer as accurately as possible:"
                )
                response = agent.run(structured_prompt)
            else:
                
                response = agent.run(user_question)

            st.markdown("### Response:")
            st.write(response.content)


if __name__ == "__main__":
    main()
