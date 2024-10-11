# PDF Summarizer with Keyword Extraction

Welcome to the **PDF Summarizer with Keyword Extraction** project! This application allows you to upload PDF files and receive concise summaries along with relevant keywords, helping you to quickly grasp the main ideas from extensive documents.

## Features

- **Upload PDF Files**: Easily upload multiple PDF files for processing.
- **Automatic Summarization**: Get concise summaries of your documents using advanced NLP techniques.
- **Keyword Extraction**: Extract relevant keywords to understand the main topics of your documents at a glance.
- **MongoDB Integration**: Store the results of your summarization and keyword extraction in a MongoDB database for future reference.

## Technologies Used

- **Python**: The programming language used for the application.
- **Streamlit**: A framework to create web applications easily.
- **PDFPlumber**: For extracting text from PDF files.
- **Sumy**: For text summarization using various algorithms.
- **NLTK**: For natural language processing tasks.
- **KeyBERT**: For keyword extraction based on BERT embeddings.
- **PyMongo**: To interact with MongoDB.

## Installation

To get started with this project, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/mangoresoham/wasserstoff.git
2. **Navigate to the project directory**:
   ```bash
   cd pdf-summarizer
3. **Create a virtual environment (optional but recommended)**:
   ```bash
   conda create -n venv python 3.8 anaconda
4. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
5. **Run the application**:
   ```bash
   streamlit run app.py
