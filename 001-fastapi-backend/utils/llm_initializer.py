from langchain_openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()

llm = OpenAI(temperature=0, openai_api_key=os.getenv("OPENAI_API_KEY"))

