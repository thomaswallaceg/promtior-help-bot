# Project Overview

## 1: RAG?

Thankfully the tutorials on LangChain's documentation made the concept pretty easy to understand and implement. I managed to set up a working local script using Ollama with llama3 that allowed me to query things about the sample webpages via console in relatively little time. Both a chain and agent based solution were implemented.

## 2: Info sources

Adding the relevant pages from the provided PDF and the links to the Promtior website was straightforward too and the required questions could now be answered by the LLM. At this point I decided to stick to the chain based solution, as the added benefit of repeat tool messages didn't impact the model's ability to answer questions about the company.

## 3: Server and interacting with it

LangServe was also easy to set up locally, after plugging in the LLM from the script into `server.py` and installing all the necessary packages with poetry the API was up and running.

I decided on a tiny Streamlit frontend for the user interaction with the server. Its simplicity, single-file implementation and ability to interact with the server via LangChain's Python client libraries (as opposed to freestyling raw API requests, which proved to be difficult) were the main factors that led me to it.

After a small foray into message persistence in the server I decided to go for a simpler solution by storing the message history in the client and passing it as part of the prompt to the API. This has some downsides (like the entire conversation being wiped on every page refresh and the size of the API requests and responses growing proportionally to the length of the conversation) but it works well for short interactions with few messages and it proved to be sufficient for the excercise's requirements.

## 4: Deploying

I initially tried to separately deploy the frontend and the backend in Railway, but ended up ditching that idea and bundling in the Streamlit frontend with the API files for them to be deployed together in a single docker container. This allows them to communicate internally in the container and simplifies the networking between them.

After waiting for some pretty long deploy times it became clear that the Ollama models would not be able to run on Railway's limited free resources, so I had to look for externally hosted alternatives with free APIs. I ended up going for a small version of llama3 hosted by Groq and an simple embeddings model hosted by Cohere. This change significantly sped up the build times (minutes to seconds) and allowed the deployed server to actually answering the prompts instead of giving timeouts.

## Bonus: Short-term improvements

- More complete deploy architecture
- Server-side persistence for conversations (including a database)
- A proper frontend that can show multiple conversations
