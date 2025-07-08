from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model = 'llama3',
             base_url= 'http://127.0.0.1:11434'
             )

result = llm.invoke('who is the current prime minister of india')

print(result.content)