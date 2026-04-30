import streamlit as st
import os
from datetime import datetime

from buscador import (
    realizar_busca_inteligente,
    obter_atalhos_e_locais,
    gerar_relatorio,
    gerar_relatorio_pdf
)

# Configuração da página
st.set_page_config(page_title="Assistente Acadêmico", layout="centered")

# Título
st.title("📚 Assistente Acadêmico ADS")
st.write("Busque materiais acadêmicos gratuitos com IA")

# Campo de entrada
with st.form("form_busca"):
    tema = st.text_input("Digite um tema:")
    submit = st.form_submit_button("Buscar")

# Botão de busca
if submit:
    if tema.strip() != "":

        with st.spinner("Buscando..."):
            resultados = realizar_busca_inteligente(tema)
            sites, bibliotecas = obter_atalhos_e_locais(tema)

        # RESULTADOS
        st.subheader("📖 Resultados")
        st.markdown(resultados)

        # ONDE OBTER
        st.subheader("✅ Onde acessar")
        st.write("https://arxiv.org")
        st.write(sites["Google Scholar"])

        # ATALHOS
        st.subheader("🔗 Atalhos")
        for nome, link in sites.items():
            st.markdown(f"- [{nome}]({link})")

        # BIBLIOTECAS
        st.subheader("🏛️ Bibliotecas")
        st.text(bibliotecas)

        # GERAR RELATÓRIO
        gerar_relatorio(tema, resultados)
        st.success("Relatório gerado com sucesso!")

        btt1, btt2 = st.columns(2)

        #  BOTÃO DE DOWNLOAD
        nome_arquivo = "relatorio_buscas.txt"

        if os.path.exists(nome_arquivo):
            with open(nome_arquivo, "r", encoding="utf-8") as f:
                conteudo = f.read()

            st.download_button(
                label="📥 Baixar relatório",
                data=conteudo,
                file_name=f"relatorio_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.txt",
                mime="text/plain"
            )
        else:
            st.warning("Relatório ainda não foi gerado.")

        # GERAR PDF
        arquivo_pdf = gerar_relatorio_pdf(tema, resultados)

        if os.path.exists(arquivo_pdf):
            with open(arquivo_pdf, "rb") as f:
                pdf_bytes = f.read()

            st.download_button(
                label="📄 Baixar relatório em PDF",
                data=pdf_bytes,
                file_name=f"relatorio_{datetime.now().strftime('%Y-%m-%d_%H-%M')}.pdf",
                mime="application/pdf"
            )

    else:
        st.warning("Digite um tema!")
