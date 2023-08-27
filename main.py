import chainlit as cl 
import openai 
import os 
#TODO - 48:43 into 2 hour video - use langchain for next section. 
os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = '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'
#return everything that the user inputs 

#pass the message into chatgpt api ... send() the answer 

@cl.on_message 
async def main(message : str): 
    response = openai.ChatCompletion.create(
        model = 'gpt-4', 
        messages = [
            {"role": "assistant" ,"content": "you are a helpful assistant"},
            {"role": "user" ,"content":message}
        ],
        temperature = 1, 
    )
    await cl.Message(content =f"{response['choices'][0]['message']['content']}",).send()
    