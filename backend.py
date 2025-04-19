import cohere
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()
co = cohere.Client(os.getenv("COHERE_API_KEY"))

def get_output(input_text):
    output = co.chat(
        model="command-a-03-2025",
        message=input_text
    )
    return output.text