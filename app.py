import streamlit as st
import os
from datetime import datetime

from buscador import (
    realizar_busca_inteligente,
    obter_atalhos_e_locais,
    gerar_relatorio
)

# Configuração da página
st.set_page_config(page_title="Assistente Acadêmico", layout="centered")

# Título
st.title("📚 Assistente Acadêmico ADS")
st.write("Busque materiais acadêmicos gratuitos com IA")

# Campo de entrada
tema = st.text_input("Digite um tema:")

# Botão de busca
if st.button("Buscar"):
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

    else:
        st.warning("Digite um tema!")
