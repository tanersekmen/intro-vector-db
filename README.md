# Intro to Vector Databases with LangChain and Pinecone

This repository provides a simple introduction to using vector databases with LangChain and Pinecone. The code demonstrates how to load text documents, split them into chunks, create embeddings using OpenAI, and store these embeddings in a Pinecone vector store. A basic RetrievalQA chain is then implemented to answer queries using the vector store.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Contributing](#contributing)

## Introduction

Vector databases are powerful tools for managing and querying embeddings generated from textual data. This project showcases a basic implementation using LangChain and Pinecone, demonstrating how to create, store, and retrieve information from a vector store using OpenAI's models.

## Requirements

To run this code, you need the following:

- Python 3.10+
- Pinecone account and API key
- OpenAI account and API key

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/tanersekmen/intro-vector-db.git
    cd intro-vector-db
    ```

2. **Install the required Python packages:**

    ```bash
    pip install langchain langchain_community langchain_openai langchain_pinecone
    ```

3. **Set up your environment variables:**

    You'll need to set up your Pinecone and OpenAI API keys as environment variables:

    ```bash
    export PINECONE_API_KEY='your-pinecone-api-key'
    export OPENAI_API_KEY='your-openai-api-key'
    ```

## Usage

To run the example code:

1. Place your text file (e.g., `text_file.txt`) in the `blog/` directory.

2. Modify the `file_path` in the `main()` function if necessary.

3. Run the script:

    ```bash
    python main.py
    ```

4. The code will process the text file, create embeddings, store them in Pinecone, and then answer the sample query: "veri bilimi nedir? kısaca açıklar mısın?"

## Code Explanation

### load_documents

This function loads the text document using the `TextLoader` from LangChain.

### split_documents

This function splits the loaded document into smaller chunks, facilitating better embedding creation and retrieval.

### create_vector_store

This function creates a vector store using Pinecone, storing the embeddings generated from the document chunks.

### create_qa_chain

This function sets up a `RetrievalQA` chain, using the vector store to retrieve relevant information based on the query.

### main

The `main()` function ties everything together, loading the documents, creating the vector store, and answering a sample query.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

