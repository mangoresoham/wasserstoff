This project is a PDF summarization and keyword extraction tool designed to help users quickly extract the essential information from large PDF documents. Users can upload multiple PDFs and receive concise summaries along with domain-specific keywords.

The project integrates multiple summarization models and approaches, and after thorough testing, the **Sumy** model was chosen due to its efficiency in environments with limited computational power, such as Hugging Face Spaces. This project also allows users to store and retrieve summaries and keywords in a MongoDB database for easy access.

Tested summarization models include **FineTuned-T5**, **PegasusXSum**, **T5-Small**, **DistilBART-CNN-12-6**, and **LLaMA3-8b-8192**, using **GPT-4** generated summaries as the reference for evaluation.
