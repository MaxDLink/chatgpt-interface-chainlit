import chainlit as cl 
import openai 
import os 
from langchain import PromptTemplate, OpenAI, LLMChain 

#API KEY read in from env variable
os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = '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'

#random string that allows LLM to think step by step 
template = """Question: {question} 

Answer: Let's think step by step.""" 

@cl.on_chat_start 
def main(): 
    prompt = PromptTemplate(template = template, input_variables = ["question"])
    llm_chain = LLMChain( #LLM object that links prompt to LLM 
        prompt = prompt, 
        llm = OpenAI(temperature = 1, streaming = True), 
        verbose = True, #additional texts to help llm with reasoning 
        
    )
    cl.user_session.set("llm_chain", llm_chain) #usersession var called llm_chain to access llm on session call 
    
    
@cl.on_message
async def main(message : str):
    llm_chain = cl.user_session.get("llm_chain") #get llm_chain from user_session
    
    res = await llm_chain.acall(message, callbacks = [cl.AsyncLangchainCallbackHandler()])
    
    await cl.Message(content = res["text"]).send()





 