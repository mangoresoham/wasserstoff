# PDF Summarizer with Keyword Extraction

Welcome to the **PDF Summarizer with Keyword Extraction** project! This application allows you to upload PDF files and receive concise summaries along with relevant keywords, helping you to quickly grasp the main ideas from extensive documents.

## Live Demo

The application is hosted on Hugging Face Spaces. You can try it out here: [PDF Summarizer on Hugging Face Spaces](https://huggingface.co/spaces/mangoresoham/PDF-Summarizer)

## Features

- **Upload PDF Files**: Easily upload multiple PDF files for processing.
- **Automatic Summarization**: Get concise summaries of your documents using advanced NLP techniques.
- **Keyword Extraction**: Extract relevant keywords to understand the main topics of your documents at a glance.
- **MongoDB Integration**: Store the results of your summarization and keyword extraction in a MongoDB database for future reference.

## Model Evaluation

In this project, several summarization models were tested to determine the most efficient and effective one for use within Hugging Face Spaces:

- **Llama3-8B-8192**: Best and fastest model for summarization and keyword extraction but is a paid service.
- **FineTuned-T5**: High-quality summarization but resource-intensive.
- **PegasusXUM**: Offers good summarization but requires significant computational resources.
- **T5-Small**: Lightweight but sacrifices some quality for speed.
- **DistilBART-CNN-12-6**: Balances quality and speed but is still resource-consuming.
- **Sumy**: Chosen for summarization in this project due to its efficiency.

## Advantages of Using Sumy for Summarization:

1. **Resource-Efficient**: Sumy is less resource-intensive compared to other models, making it ideal for deployment in environments like Hugging Face Spaces.
2. **Fast Processing**: It provides quicker summarization results, which is essential for user experience, especially when handling large documents.
3. **Ease of Use**: Sumy has a straightforward python library that makes it easy to implement and integrate into applications.
4. **Multiple Algorithms**: Sumy supports various summarization algorithms, allowing for flexibility based on the document type and requirements.
5. **Quality Summaries**: Despite being lightweight, Sumy still delivers satisfactory quality in the summaries it generates.

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
