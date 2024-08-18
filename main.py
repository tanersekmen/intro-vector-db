import os
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain_openai import OpenAIEmbeddings, OpenAI
from langchain_pinecone import PineconeVectorStore
from langchain_text_splitters import CharacterTextSplitter
from langchain.chains import VectorDBQA

def load_documents(file_path, encoding = 'UTF-8'):
    loader = TextLoader(file_path = file_path, encoding=encoding)
    return loader.load()


def split_documents(documents, chunk_size = 100, chunk_overlap = 10):
    text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.split_documents(documents)


def create_vectore_store(docs, index_name, embeddings):
    return PineconeVectorStore.from_documents(docs, index_name=index_name, embedding=embeddings)


def create_qa_chain(vector_store):
    return RetrievalQA.from_chain_type(
        llm = OpenAI(),
        chain_type='stuff',
        retriever = vector_store.as_retriever(),
        return_source_documents = True
    )

def main():
    PINECONE_API_KEY = os.getenv('PINECONE_API_KEY')
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    index_name = 'first-app'
    file_path = 'blog/text_file.txt'

    embeddings = OpenAIEmbeddings()
    documents = load_documents(file_path)
    docs = split_documents(documents)

    vector_store = create_vectore_store(docs, index_name, embeddings)

    qa = create_qa_chain(vector_store)

    query = 'veri bilimi nedir? kısaca açıklar mısın?'

    result = qa({'query':query})
    print(result)


if __name__ == '__main__':
    main()