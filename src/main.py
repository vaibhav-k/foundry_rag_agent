"""
Entry point for the Foundry RAG Agent system.

This script orchestrates the full lifecycle:

1. Initializes Azure AI Foundry client
2. Resolves Azure AI Search connection
3. Creates RAG-enabled agent
4. Runs interactive chat session
5. Cleans up agent after use

This ensures resources are not left dangling in Azure.
"""

from client import get_project_client
from search_connection import get_search_connection_id
from agent_service import create_agent, delete_agent
from chat_service import run_chat
from config import SEARCH_CONNECTION_NAME


def main():
    """
    Main execution pipeline for RAG agent workflow.
    """

    project = get_project_client()

    connection_id = get_search_connection_id(
        project,
        SEARCH_CONNECTION_NAME,
    )

    agent = create_agent(project, connection_id)

    try:
        run_chat(project, agent)
    finally:
        delete_agent(project, agent)


if __name__ == "__main__":
    main()
