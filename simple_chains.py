from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model = 'llama3',
             base_url= 'http://127.0.0.1:11434'
             )

prompt = PromptTemplate(
    template='generate 5 intresting facts about {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

#result = chain.invoke({'topic':'cricket'})

#print(result)

chain.get_graph().print_ascii()