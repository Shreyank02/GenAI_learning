from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gpt-4', temperature=1)

result = model.invoke('What is the capital of india')

print(result)
print(result.content)