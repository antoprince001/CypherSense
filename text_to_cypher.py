import os
from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
graph = Neo4jGraph(url=os.environ['NEO4J_URL'], username=os.environ['NEO4J_USERNAME'], password=os.environ['NEO4J_PASSWORD'], database='movie')

graph.refresh_schema()
chain = GraphCypherQAChain.from_llm(
    ChatGoogleGenerativeAI(
            model="gemini-1.5-flash", google_api_key=os.environ['GOOGLE_API_KEY']
        ), graph=graph, verbose=True, allow_dangerous_requests=True
)

# chain.run("How many actors are there?")
print(chain.run("Actors part of Matrix?"))
