"""
Configuration module for the Foundry RAG Agent system.

This module centralizes all static configuration values such as:
- Azure AI Foundry project endpoint
- Azure AI Search connection name
- Search index name
- Agent model and behavior instructions

Keeping configuration in one place allows easy switching between:
- environments (dev / test / prod)
- different search indexes
- different Foundry projects
"""

import os

PROJECT_ENDPOINT = os.getenv("PROJECT_ENDPOINT")

SEARCH_CONNECTION_NAME = os.getenv("SEARCH_CONNECTION_NAME")
SEARCH_INDEX_NAME = os.getenv("SEARCH_INDEX_NAME")

AGENT_NAME = os.getenv("AGENT_NAME")
MODEL_NAME = os.getenv("MODEL_NAME")

INSTRUCTIONS = """
You are a helpful assistant working with Azure AI Search (RAG).

Rules:
- Always use retrieved context when answering.
- Always include citations in format: [message_idx:search_idx†source].
- If unsure, say you don't have enough information.
"""
