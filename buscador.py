import os
# Importamos a conexão com o Ollama que você baixou (o 'cabo' que liga o Python à IA)
from langchain_ollama import OllamaLLM
# Importamos o buscador do ArXiv (nosso acervo de livros e artigos gratuitos)
from langchain_community.utilities import ArxivAPIWrapper
from datetime import datetime
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# 1. CONFIGURAÇÃO DO CÉREBRO (IA LOCAL)
# Aqui dizemos ao Python para usar o modelo leve que baixamos para não travar seu PC
llm = OllamaLLM(model="llama3.2:1b")

# 2. CONFIGURAÇÃO DO BUSCADOR
# Instanciamos o buscador que acessa o banco de dados acadêmico
buscador_academico = ArxivAPIWrapper(top_k_results=3)

def realizar_busca_inteligente(tema):
    """
    Esta função recebe o que o usuário quer e usa a IA para 
    criar uma busca melhor (Requisito 1 da atividade).
    """
    print(f"\n[Monitor ADS] Analisando o tema: {tema}...")
    
    prompt = f"keywords: {tema}. Return only 3 keywords in English, no text."
    keywords = llm.invoke(prompt).strip() # .strip() remove espaços vazios inúteis
    
    print(f"[IA] Buscando por: {keywords}")    
    # Agora o buscador usa essas palavras para trazer os livros/artigos
    # O ArXiv foca em materiais gratuitos (Requisito 4)
    resultados = buscador_academico.run(keywords)
    
    return resultados

def obter_atalhos_e_locais(tema):
    """
    Propicia atalhos de sites e informações de bibliotecas (Requisitos 2 e 3).
    """
    # Atalhos automáticos de acervos gratuitos (Requisito 2)
    atalhos = {
        "SciELO": "https://scielo.org",
        "Open Library": "https://openlibrary.org",
        "Directory of Open Access Books (DOAB)": "https://www.doabooks.org",
        "Google Scholar": f"https://scholar.google.com.br/scholar?q={tema}+filetype:pdf"
    }
    
    # Simulação de busca em Bibliotecas Públicas (Requisito 3)
    # Em um sistema real, usaríamos a localização do IP. Aqui, daremos o caminho.
    info_bibliotecas = (
        f"1. Biblioteca Pública Estadual (Consulte o acervo local para: {tema})\n"
        f"2. Biblioteca do IF (Instituto Federal) - Acervo de Tecnologia\n"
        f"3. Sistema Nacional de Bibliotecas Públicas (SNBP): http://snbp.cultura.gov.br/"
    )
    
    return atalhos, info_bibliotecas

# Gerar PDF
def gerar_relatorio(tema, resultados):
    """
    Registra a busca em um arquivo de log histórico (Requisito 5).
    """
    data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    nome_arquivo = "relatorio_buscas.txt"
    
    # Abrimos o arquivo no modo 'a' (append), que adiciona ao final sem apagar o que já existe
    with open(nome_arquivo, "a", encoding="utf-8") as arquivo:
        arquivo.write("=" * 60 + "\n")
        arquivo.write(f"SESSÃO DE ESTUDOS: {data_atual}\n")
        arquivo.write(f"TEMA PESQUISADO: {tema}\n")
        arquivo.write("-" * 60 + "\n")
        arquivo.write("CONTEÚDO ENCONTRADO:\n\n")
        arquivo.write(resultados) # Aqui vai os 3 artigos completos
        arquivo.write("\n" + "=" * 60 + "\n\n")
    
    print(f"\n[Sistema] Relatório atualizado com sucesso em: {nome_arquivo}")

def gerar_relatorio_pdf(tema, resultados):
    nome_arquivo = "relatorio_buscas.pdf"

    doc = SimpleDocTemplate(nome_arquivo)
    styles = getSampleStyleSheet()

    conteudo = []

    conteudo.append(Paragraph("Assistente Acadêmico ADS", styles["Title"]))
    conteudo.append(Spacer(1, 12))

    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    conteudo.append(Paragraph(f"Data: {data}", styles["Normal"]))
    conteudo.append(Spacer(1, 12))

    conteudo.append(Paragraph(f"Tema: {tema}", styles["Heading2"]))
    conteudo.append(Spacer(1, 12))

    conteudo.append(Paragraph("Resultados:", styles["Heading3"]))
    conteudo.append(Spacer(1, 12))

    resultados_formatados = resultados.replace("\n", "<br/>")
    conteudo.append(Paragraph(resultados_formatados, styles["Normal"]))

    doc.build(conteudo)

    return nome_arquivo

# 3. INTERFACE DO PROGRAMA (O QUE VOCÊ VÊ NA TELA)
if __name__ == "__main__":
    print("=== ASSISTENTE ACADÊMICO ADS ===")
    assunto = input("O que você deseja estudar hoje? ")
    
    # 1. Realiza a busca via IA
    resultados_ia = realizar_busca_inteligente(assunto)
    
    # 2. Obtém atalhos e bibliotecas
    sites, bibliotecas = obter_atalhos_e_locais(assunto)
    
    # 3. Exibe na tela (Interface do usuário)
    print("\n" + "="*50)
    print("RESULTADOS ENCONTRADOS")
    print(resultados_ia)
    
    print("\nONDE OBTER LEGALMENTE:")
    print(f"1. Acesse https://arxiv.org e cole o título do artigo acima.")
    print(f"2. Use o link do Google Scholar abaixo para encontrar o PDF direto.")

    # 4. GERA O RELATÓRIO AUTOMÁTICO (Requisito 5)
    gerar_relatorio(assunto, resultados_ia)
    
    print("\n=== ATALHOS E BIBLIOTECAS ===")
    for nome, link in sites.items():
        print(f"- {nome}: {link}")
    
    print("\n" + "="*50)
    print("Dica Legal: Conteúdo distribuído legalmente.")