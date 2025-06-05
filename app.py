import streamlit as st

st.title("Estatística e Probabilidade")
st.write("Projeto de estatística voltado para análise exploratória de bases de dados relacionadas a ocorrências de crimes na cidade de Los Angeles, CA a partir do ano de 2020.")

bases, analises, relatorio = st.columns(3)
with bases.container(border=True):
    st.button(label=":material/database: Docs e Bases")
    st.write("Bases, bibliotecas e tecnologias utilizadas no projeto.")
with analises.container(border=True):
    st.button(label=":material/edit_note: Análises Realizadas")
    st.write("Análises exploratórias realizadas, questionamentos e cálculos estatísticos.")
with relatorio.container(border=True):
    st.button(label=":material/newspaper: Relatório Final")
    st.write("Correlações, informações e conclusões encontradas no decorrer do projeto.")

st.title("Integrantes do Grupo")
beatriz, felipe, joao = st.columns(3)
with beatriz.container(border=True):
    st.header("Beatriz", divider=True)
    st.subheader("SP3161315")
    linkedin_url_beatriz = "https://www.linkedin.com/in/beatrizmunizz/"
    github_url_beatriz = "https://github.com/beamuniz"
    st.markdown(f"[:material/open_in_new: LinkedIn]({linkedin_url_beatriz}) &nbsp;&nbsp; [:material/open_in_new: GitHub]({github_url_beatriz})")
with felipe.container(border=True):
    st.header("Felipe", divider=True)
with joao.container(border=True):
    st.header("João", divider=True)
    st.subheader("SP3137627")
    linkedin_url_joao = "https://www.linkedin.com/in/j-pedro-rodrigues/"
    github_url_joao = "https://github.com/P-Joao"
    st.markdown(f"[:material/open_in_new: LinkedIn]({linkedin_url_joao}) &nbsp;&nbsp; [:material/open_in_new: GitHub]({github_url_joao})")