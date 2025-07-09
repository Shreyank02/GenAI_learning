from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_community.chat_models import ChatOllama

model = ChatOllama(model = 'llama3',
             base_url= 'http://127.0.0.1:11434'
             )

messages=[
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about mcp server')
]

result = model.invoke(messages)

messages.append(AIMessage(content=result.content))

print(messages)