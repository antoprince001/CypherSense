import chainlit as cl
from dotenv import load_dotenv
import text_to_cypher

load_dotenv()


@cl.on_message
async def main(message: cl.Message):
    response = text_to_cypher.text_to_cypher_chain.invoke(message.content)
    await cl.Message(
        content=response,
    ).send()
