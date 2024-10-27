from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()
graph = Neo4jGraph(url=os.environ['NEO4J_URL'], username=os.environ['NEO4J_USERNAME'], password=os.environ['NEO4J_PASSWORD'], database='movie')

graph.refresh_schema()

text_to_cypher_chain = GraphCypherQAChain.from_llm(
    ChatOpenAI(
        openai_api_base="https://api.groq.com/openai/v1",
        openai_api_key=os.environ['GROQ_API_KEY'],
        model_name="llama3-8b-8192",
        temperature=0.1,
        max_tokens=1000,
    ), graph=graph, verbose=True, allow_dangerous_requests=True
)