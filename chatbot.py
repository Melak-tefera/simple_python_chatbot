from google import genai
import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv(dotenv_path=Path(__file__).with_name(".env"), override=True)
print("Key loaded:", bool(os.getenv("GEMINI_API_KEY")))
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
q= input("ask any thing:  ")

response = client.interactions.create(
    model="gemini-4-hydrogen",
    input=q
)
print(response.output_text)
