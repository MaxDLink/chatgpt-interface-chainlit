import chainlit as cl 
import openai 
import os 

# Read the API key from the local .txt file and assign it to the environment variable
openai.api_key_path = "api_key.txt"
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
    