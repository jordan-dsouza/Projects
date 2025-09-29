##Libraries:
1. !pip install --upgrade --quiet langchain-google-genai

* Purpose: Installs the LangChain integration for Google's Gemini API.
* Use: Enables calling _Gemini models_ and _embeddings_ within LangChain workflows.

2. !pip install --upgrade --quiet langchain-community

* Purpose: Installs community-contributed LangChain modules and integrations.
* Use: Required for using tools like FAISS, Chroma, or other wrappers within LangChain.

3. !pip install --upgrade --quiet faiss-cpu

* Purpose: Installs FAISS, Facebook’s _vector similarity search_ library.
* Use: Allows _semantic search over document embeddings_ (core to Retrieval-Augmented Generation).

4. !pip install --quiet pypdf

* Purpose: Lightweight library to _read and extract text from PDF_ documents.
* Use: Used for parsing research papers as input to the AI.

5. from langchain.vectorstores import FAISS
   
* Purpose: To enable _fast vector similarity search_ using FAISS (Facebook AI Similarity Search).
* Use: Store and search document embeddings to _retrieve relevant chunks_ for a given query.

6. from langchain_google_genai import GoogleGenerativeAIEmbeddings

* Purpose: To access Google's Gemini embedding model through LangChain.
* Use: Convert _chunks of text_ into _high-dimensional embedding vectors_ for _similarity_ search.

7. from langchain.text_splitter import CharacterTextSplitter

* Purpose: To break large documents into smaller, overlapping text chunks.
* Use: Ensures that the input to the embedding model is within _token limits_ and _contextually complete_.

8. from langchain.docstore.document import Document

* Purpose: To wrap individual chunks of text with metadata (e.g., page number, source).
* Use: Enables _easier tracking_ of where a retrieved chunk came from (for citation or explanation).


##Code:
1. PdfReader reads pdf and extracts text.
2. *Chunking* breaks down complex information into small chunks to improve memory with maximum 1500 tokens.
3. A *Question* is asked using a *Prompt* and *Context*. '*.invoke*' allows to send input and receive response.
4. Paper is summarized and trimmed down to 10000 words.
5. For [RAG](**RAG**), document is split and stored with embeddings in vector database.
6. Using similarity search, top k contextual chunks are retrieved.


##Definitions:
1. **RAG**: Retrieval-Augmented Generation (RAG) is the process of optimizing the output of a large language model, so it references an authoritative knowledge base outside of its training data sources before generating a response.
2. 
