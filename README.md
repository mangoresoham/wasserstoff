This repository contains a domain-specific PDF summarization and keyword extraction pipeline designed to efficiently process multiple PDF documents of varying lengths. The pipeline ingests PDF files, generates concise domain-specific summaries, extracts relevant keywords, and stores the results in a MongoDB database. 

The system was developed to handle documents of varying lengths, including short (1-10 pages), medium (10-30 pages), and long (30+ pages) PDFs, and ensures efficient parallel processing to manage large files without crashing. The summarization process dynamically adjusts based on document length, producing detailed summaries for longer documents and concise ones for shorter documents.

Key functionalities:
- **PDF Ingestion & Parsing**: Supports batch processing of multiple PDFs from a folder.
- **Summarization & Keyword Extraction**: Domain-specific summaries and keywords generated using custom and resource-efficient methods.
- **MongoDB Storage**: Document metadata and processing results are stored in MongoDB with JSON formatting.
- **Concurrency & Performance**: Leverages parallel processing for fast, efficient summarization of large volumes of documents.
  
This project was completed as part of an AI internship task at **Wasserstoff Innovation & Learning Labs Private Limited**.

### Important Note on Concurrency

Streamlit uses the Tornado web server, which operates in a single-threaded environment. While this design allows for real-time updates and interactive features, it also limits the ability to perform parallel processing within the application. 

As a result, features like batch processing or multi-threading for faster document summarization and keyword extraction are best suited for local environments. Users running the application in Hugging Face Spaces will not benefit from parallel processing capabilities, which can affect the performance and speed of processing larger documents.
