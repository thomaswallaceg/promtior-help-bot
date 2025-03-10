import os
from dotenv import load_dotenv

load_dotenv()

if not os.environ.get("GROQ_API_KEY"):
    raise Exception("Missing GROQ_API_KEY")
if not os.environ.get("COHERE_API_KEY"):
    raise Exception("Missing COHERE_API_KEY")

cohere_api_key = os.environ.get("COHERE_API_KEY")

os.environ.setdefault("USER_AGENT", "user_agent")

from langchain.chat_models import init_chat_model
from langchain_cohere import CohereEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

llm = init_chat_model("llama3-70b-8192", model_provider="groq")
embeddings = CohereEmbeddings(model="embed-english-v3.0", cohere_api_key=cohere_api_key)
vector_store = InMemoryVectorStore(embeddings)

import bs4
from langchain_community.document_loaders import WebBaseLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf_loader = PyPDFLoader('app/utils/AI Engineer.pdf')
pages = []
for page in pdf_loader.load():
    pages.append(page)
# Filter PDF pages with actual Promtior info
pages = [pages[0], pages[2], pages[3], pages[9]]

# Load contents
web_loader = WebBaseLoader(
    web_paths=("https://www.promtior.ai/", "https://www.promtior.ai/use-cases", "https://www.promtior.ai/service"),
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer(
            class_=("post-content", "post-title", "post-header")
        )
    ),
)
docs = web_loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
all_splits = text_splitter.split_documents(pages + docs)

vector_store.add_documents(documents=all_splits)
