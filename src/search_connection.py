"""
Azure AI Search connection resolution module.

This module resolves the Azure AI Search connection ID from the Foundry project.
The connection ID is required to link the agent with an Azure AI Search index.

Without this connection, the agent cannot perform retrieval-augmented generation (RAG).
"""


def get_search_connection_id(project, connection_name: str) -> str:
    """
    Retrieve Azure AI Search connection ID from the Foundry project.

    Args:
        project (AIProjectClient): Authenticated Foundry project client.
        connection_name (str): Name of the Azure AI Search connection.

    Returns:
        str: Fully qualified connection ID used by Azure AI Search tool.

    Raises:
        KeyError: If the connection is not found in the project.
    """
    connection = project.connections.get(connection_name)

    print(f"[INFO] Using Search Connection: {connection.name}")

    return connection.id
