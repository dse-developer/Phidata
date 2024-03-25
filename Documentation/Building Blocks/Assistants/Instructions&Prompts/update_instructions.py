from dotenv import load_dotenv
load_dotenv()

from phi.assistant import Assistant

assistant = Assistant(
    description="You are a famous short story writer that has been asked to write for a magazine",
    instructions=["You are a pilot on a plane flying from Hawaii to Japan."],
    markdown=True,
    prevent_prompt_injection=True,
    debug_mode=True,
)
assistant.print_response("Tell me a 2 sentence horror story.")