import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon=":material/home:",
)

st.title("Estatística e Probabilidade")
st.write("Projeto de estatística voltado para análise exploratória de bases de dados relacionadas a ocorrências de crimes na cidade de Los Angeles, CA a partir do ano de 2020.")

bases, analises, relatorio = st.columns(3)
with bases.container(border=True):
    if st.button(label=":material/database: Docs e Bases"):
        st.switch_page("pages/Docs_e_Bases.py")
    st.write("Bases, bibliotecas e tecnologias utilizadas no projeto.")
with analises.container(border=True):
    if st.button(label=":material/edit_note: Análises Realizadas"):
        st.switch_page("pages/Analises.py")
    st.write("Análises exploratórias realizadas, questionamentos e cálculos estatísticos.")
with relatorio.container(border=True):
    if st.button(label=":material/newspaper: Relatório Final"):
        st.switch_page("pages/Relatorio_Final.py")
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
    st.subheader("SP3155048")
    linkedin_url_felipe = "https://www.linkedin.com/in/felipe-teixeira-de-lima/"
    github_url_felipe = "https://github.com/felipeteixeiradelima"
    st.markdown(f"[:material/open_in_new: LinkedIn]({linkedin_url_felipe}) &nbsp;&nbsp; [:material/open_in_new: GitHub]({github_url_felipe})")
with joao.container(border=True):
    st.header("João", divider=True)
    st.subheader("SP3137627")
    linkedin_url_joao = "https://www.linkedin.com/in/j-pedro-rodrigues/"
    github_url_joao = "https://github.com/P-Joao"
    st.markdown(f"[:material/open_in_new: LinkedIn]({linkedin_url_joao}) &nbsp;&nbsp; [:material/open_in_new: GitHub]({github_url_joao})")