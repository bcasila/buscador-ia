📚 Assistente Acadêmico com IA

Sistema para busca de livros e materiais acadêmicos gratuitos, utilizando IA local e interface web interativa.

# FUNCIONALIDADES
-- Busca inteligente de conteúdos acadêmicos
-- Uso de IA local com Ollama
-- Integração com ArXiv (materiais gratuitos)
-- Atalhos para plataformas como SciELO, DOAB e Google Scholar
--Sugestões de bibliotecas públicas
-- Geração automática de relatórios
-- Download do relatório diretamente pela interface
# PRIMEIRO ACESSO

1. Baixe e instale o Ollama:
https://ollama.com

2. Após instalar, abra o terminal e execute:

    ollama run llama3

Se der erro por falta de memória RAM, use:

    ollama run llama3.2:1b

Esse comando baixará o modelo de IA que rodará no seu computador.

3. Abra a pasta do projeto no terminal e, se necessário no Windows, execute:

    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

4. Ative o ambiente virtual:

    .\venv\Scripts\activate

Quando aparecer (venv), instale todas as dependências necessárias:

    pip install langchain
    pip install langchain-community
    pip install langchain-ollama
    pip install arxiv
    pip install geopy
    pip install pandas

Ou tudo de uma vez:

    pip install langchain langchain-community langchain-ollama arxiv geopy pandas


# PRÓXIMOS ACESSOS

Abra o terminal na pasta do projeto e execute:

    .\venv\Scripts\activate


# PARA INICIAR O BUSCADOR

    python buscador.py


# PARA SAIR DO AMBIENTE VIRTUAL

    deactivate
# COMO EXECUTAR O SISTEMA (INTERFACE WEB)
 1. Iniciar o Ollama
ollama run llama3.2:1b
 2. Executar o frontend com Streamlit
streamlit run app.py

- Esse comando irá abrir automaticamente o sistema no navegador.

 3. Acessar no navegador (caso não abra automaticamente)

http://localhost:8501

# Observações
- O Ollama precisa estar rodando para que a IA funcione corretamente
- A busca pode ser mais lenta devido ao processamento local da IA
- O sistema prioriza conteúdos acadêmicos gratuitos e de acesso legal
