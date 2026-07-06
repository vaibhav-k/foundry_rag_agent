"""
Azure AI Foundry client factory module.

This module is responsible for creating and configuring the AIProjectClient,
which is the main entry point for interacting with Azure AI Foundry services.

It uses DefaultAzureCredential for authentication, which supports:
- Azure CLI login
- Managed Identity (cloud deployments)
- Environment variables
- Visual Studio Code login (if configured)
"""

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from config import PROJECT_ENDPOINT


def get_project_client() -> AIProjectClient:
    """
    Creates and returns an authenticated Azure AI Foundry project client.

    Returns:
        AIProjectClient: Authenticated client for Foundry operations.
    """
    return AIProjectClient(
        endpoint=PROJECT_ENDPOINT,
        credential=DefaultAzureCredential(),
    )
