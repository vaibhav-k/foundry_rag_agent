"""
Agent creation and lifecycle management module.

This module defines and manages Azure AI Foundry agents that are configured
with Azure AI Search tools for Retrieval-Augmented Generation (RAG).

Responsibilities:
- Create agent versions
- Attach Azure AI Search tool
- Delete agent versions when no longer needed
"""

from azure.ai.projects.models import (
    AzureAISearchTool,
    PromptAgentDefinition,
    AzureAISearchToolResource,
    AISearchIndexResource,
    AzureAISearchQueryType,
)

from config import (
    AGENT_NAME,
    MODEL_NAME,
    INSTRUCTIONS,
    SEARCH_INDEX_NAME,
)


def create_agent(project, connection_id: str):
    """
    Creates a new Azure AI Foundry agent with Azure AI Search tool enabled.

    Args:
        project (AIProjectClient): Foundry project client.
        connection_id (str): Azure AI Search connection ID.

    Returns:
        Agent: Created agent instance.
    """

    agent = project.agents.create_version(
        agent_name=AGENT_NAME,
        definition=PromptAgentDefinition(
            model=MODEL_NAME,
            instructions=INSTRUCTIONS,
            tools=[
                AzureAISearchTool(
                    azure_ai_search=AzureAISearchToolResource(
                        indexes=[
                            AISearchIndexResource(
                                project_connection_id=connection_id,
                                index_name=SEARCH_INDEX_NAME,
                                query_type=AzureAISearchQueryType.SIMPLE,
                            )
                        ]
                    )
                )
            ],
        ),
        description="RAG-enabled Azure AI Foundry agent",
    )

    print(f"[INFO] Agent created: {agent.name} (v{agent.version})")
    return agent


def delete_agent(project, agent):
    """
    Deletes a specific agent version from the Foundry project.

    Args:
        project (AIProjectClient): Foundry project client.
        agent (Agent): Agent instance to delete.
    """
    project.agents.delete_version(
        agent_name=agent.name,
        agent_version=agent.version,
    )

    print(f"[INFO] Agent deleted: {agent.name} (v{agent.version})")
