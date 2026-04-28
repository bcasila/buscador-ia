# Assistente de Busca Acadêmica com IA (ADS)
Este projeto é um agente de inteligência artificial local projetado para buscar materiais acadêmicos, 
livros e artigos de forma gratuita e legal.

# Tecnologias Utilizadas
O projeto foi construído utilizando uma arquitetura moderna de agentes de IA:
Linguagem: Python 3.10+ - Base para toda a lógica de automação e integração.
Orquestração de IA: LangChain - Framework que conecta o modelo de linguagem (LLM) às ferramentas de busca externa.
Modelo de Linguagem (LLM): Ollama (Llama 3.2 1B) - Processamento de linguagem natural rodando localmente para 
garantir privacidade e baixo custo.
Busca Acadêmica: ArXiv API - Repositório científico utilizado para buscar artigos e livros técnicos gratuitos.
Manipulação de Dados: Pandas e [Datetime] - Para organização das informações e geração dos relatórios de log.

# Requisitos de Instalação
1. Motor de IA (Ollama)
O projeto utiliza o Ollama para rodar modelos de linguagem localmente.
Baixe e instale o Ollama em ollama.com.
No terminal, baixe o modelo leve (ideal para máquinas com até 8GB de RAM):
    ollama run llama3.2:1b
2. Ambiente Python
Com o Python instalado, siga os passos na pasta do projeto:
Configurar permissão (Windows): Caso o script de ativação seja bloqueado, execute no PowerShell:
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
Criar e Ativar o Ambiente Virtual:
    python -m venv venv
    .\venv\Scripts\activate
Instalar Dependências:
    pip install langchain langchain-community langchain-ollama arxiv geopy pandas

# Como Utilizar
Iniciar o Sistema
Sempre que desejar usar o buscador, certifique-se de que o Ollama está aberto e execute:
Ative o ambiente: .\venv\Scripts\activate
Rode o programa: python buscador.py

Funcionalidades
Busca Inteligente: IA converte temas em palavras-chave técnicas.
Acervos Gratuitos: Filtros automáticos para materiais Open Access.
Relatórios: Cada busca gera um log automático no arquivo relatorio_buscas.txt.

Finalizar
Para encerrar o ambiente virtual:
    deactivate
