from dotenv import load_dotenv
load_dotenv()

from phi.assistant.openai import OpenAIAssistant
from phi.assistant.openai.file.url import UrlFile
from phi.assistant.openai.tool import CodeInterpreter

# Load the IMDB dataset from S3
imdb_movie_data_s3 = UrlFile(url="https://phi-public.s3.amazonaws.com/imdb/IMDB-Movie-Data.csv").get_or_create()

# Create an Assistant
with OpenAIAssistant(
    name="CsvAssistant",
    tools=[CodeInterpreter],
    files=[imdb_movie_data_s3],
    instructions="You are an expert at analyzing CSV data. Whenever you run an analysis, explain each step.",
) as csv_assistant:
    # Run the Assistant
    csv_assistant.print_response("Who is the most popular actor by votes?")
