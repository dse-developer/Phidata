from dotenv import load_dotenv
load_dotenv()

from phi.assistant import Assistant
from phi.tools.python import PythonTools

assistant = Assistant(tools=[PythonTools()], show_tool_calls=True)
assistant.print_response("Summarize the top stories on hackernews")
