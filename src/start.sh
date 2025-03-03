#!/bin/bash

poetry run langchain serve --port 8080 &
poetry run streamlit run app/ui.py --server.port 8081 --server.address 0.0.0.0
