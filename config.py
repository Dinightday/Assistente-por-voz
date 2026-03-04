from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class Baseconfig():
    def __init__(self, modelo):
        self._api_openai = os.environ["OPENAI_API_KEY"]
        self._api_tavily = os.environ["TAVILY_API_KEY"]
        self.llm = ChatOpenAI(
            model=modelo, 
            temperature=0.3, 
            api_key=self._api_openai)