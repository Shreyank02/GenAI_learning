from langchain_community.chat_models import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

model = ChatOllama(model = 'llama3',
             base_url= 'http://127.0.0.1:11434'
             )

chat_history = [
    SystemMessage(content='You are a helpful assistant')
]

while True:
    user_input = input('You : ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI : ",result.content)

print(chat_history)