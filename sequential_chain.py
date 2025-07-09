from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatOllama(model = 'llama3',
             base_url= 'http://127.0.0.1:11434'
             )


parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

#result = chain.invoke({'topic': 'Unemployment in India'})

#print(result)

chain.get_graph().print_ascii()