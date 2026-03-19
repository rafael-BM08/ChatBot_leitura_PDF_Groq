import os
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader

api_key = 'API GROQ AQUI'

os.environ['GROQ_API_KEY'] = api_key

chat = ChatGroq(model='llama-3.3-70b-versatile')

caminho = 'D:\\ChatBot_Get_pessoas\\funcionarios.pdf'

loader = PyPDFLoader(caminho)

lista_documentos = loader.load()

documento = ''

for doc in lista_documentos:
    documento = documento + doc.page_content

def resposta_bot(mensagens, documento):
    mensagens_modelo = [('system', f'Você é um assistente chamado Caeso. Use o documento a seguir para responder perguntas sobre funcionários: {documento}. Responda APENAS o que foi perguntado, de forma curta e direta. Não forneça informações extras que não foram solicitadas.')]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    chain = template | chat
    return chain.invoke({'informações': documento }).content



print("\nBem-Vindo ao ChatBot CAESO\n")

mensagens = []

while True:
    pergunta = input('Usuario: ')
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens, documento)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')

print('Muito obrigado por usar o ChatBot Caeso')
print(mensagens)
  

  

  

  