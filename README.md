# Genie: Your AI-powered Insight Generator from PDFs

Genie is a powerful Streamlit application designed to extract and analyze text from PDF documents, leveraging the advanced capabilities of large language models (LLMs). This tool uses a Retrieval-Augmented Generation (RAG) framework to offer precise, context-aware answers to user queries based on the content of uploaded documents.

## Features

- **Instant Insights**: Extracts and analyzes text from uploaded PDF documents to provide instant insights.
- **Retrieval-Augmented Generation**: Utilizes advanced generative AI models for high-quality, contextually relevant answers.
- **Secure API Key Input**: Ensures secure entry of API keys for accessing generative AI models.
- **User-Friendly Interface**: Built with Streamlit for an interactive user experience.

## Getting Started

### Prerequisites

- **Python**: Ensure you have Python 3.7 or higher installed.
- **API Key**: Obtain an API key for any external services you plan to use (e.g., OpenAI, Google API).

### Installation

1. Clone this repository or download the source code to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create a virtual environment (optional but recommended).
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # For macOS/Linux
   myenv\Scripts\activate  # For Windows
   ```

3. Install the required Python packages.
   ```bash
   pip install -r requirements.txt
   ```

### How to Use

1. **Start the Application**: Launch the Streamlit application by running the command:
   ```bash
   streamlit run streamlit_App.py
   ```

2. **Enter Your API Key**: Securely enter your API key when prompted. This key enables the application to access generative AI models.

3. **Upload PDF Documents**: You can upload one or multiple PDF documents. The application will analyze the content of these documents to respond to queries.

4. **Ask Questions**: Once your documents are processed, you can ask any question related to the content of your uploaded documents.

## Technical Overview

- **PDF Processing**: Utilizes `PyPDF2` for extracting text from PDF documents.
- **Text Chunking**: Employs the `RecursiveCharacterTextSplitter` from LangChain for dividing the extracted text into manageable chunks.
- **Vector Store Creation**: Uses `FAISS` for creating a searchable vector store from text chunks.
- **Answer Generation**: Leverages `transformers` and other libraries for generating answers to user queries using the context provided by the uploaded documents.

## Support

For issues, questions, or contributions, please refer to the GitHub repository issues section or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
