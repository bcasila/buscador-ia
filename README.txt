# Primeiro acesso:
Baixe o Ollama em ollama.com
Após instalar, abra o terminal e digite: 
    ollama run llama3
ou, se der erro por memória RAM, use:
    ollama run llama3.2:1b
Isso baixará o "cérebro" que rodará no seu hardware.
Se der erro, faça isso para o windows reconhecer dentro do cmd:
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
Após isso:
    .\venv\Scripts\activate
Assim que o (venv) aparecer, precisamos instalar as ferramentas que expliquei anteriormente. 
Copie e cole este comando único:
    pip install langchain langchain-community langchain-ollama arxiv geopy pandas


# Outros acessos:
No cmd Ctrl+' :
    .\venv\Scripts\activate

# Para iniciar o buscador:
    python buscador.py

# Para sair:
    deactivate