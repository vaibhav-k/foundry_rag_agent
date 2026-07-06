"""
Chat execution and streaming response handler.

This module handles:
- Sending user queries to the agent
- Streaming responses from Azure OpenAI
- Printing real-time output
- Extracting and displaying citations
"""


def run_chat(project, agent):
    """
    Executes an interactive chat session with the agent.

    Args:
        project (AIProjectClient): Foundry project client.
        agent (Agent): Active RAG-enabled agent.

    Behavior:
        - Accepts user input
        - Streams model response
        - Displays citations if available
    """

    openai = project.get_openai_client()

    print("\n--- Chat started (type 'exit' to quit) ---\n")

    while True:

        question = input("\nEnter your question:\n> ")

        # ✅ STOP CONDITION (must come first)
        if question.lower() in ["exit", "quit"]:
            print("Session ended. Goodbye.")
            break

        stream = openai.responses.create(
            stream=True,
            tool_choice="required",
            input=question,
            extra_body={
                "agent_reference": {
                    "name": agent.name,
                    "type": "agent_reference",
                }
            },
        )

        print("\n--- Response ---\n")

        for event in stream:

            if event.type == "response.output_text.delta":
                print(event.delta, end="", flush=True)

            elif event.type == "response.output_item.done":

                if event.item.type == "message":
                    text = event.item.content[-1]

                    if text.type == "output_text":
                        for annotation in text.annotations:
                            if annotation.type == "url_citation":
                                citations = []

                                if annotation.type == "url_citation":
                                    if "search.windows.net" not in annotation.url:
                                        citations.append(annotation.url)

                                if citations:
                                    print("\n\nSources:")
                                    for c in set(citations):
                                        print(f"- {c}")

            elif event.type == "response.completed":
                print("\n")
