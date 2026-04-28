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
