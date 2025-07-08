import streamlit as st

st.set_page_config(
    page_title="Relatório Final",
    page_icon=":material/newspaper:",
)

st.title("Análise Criminal na Cidade de Los Angeles")
with st.container():
    st.header("Estátistica e Probabilidade - Profa. Josceli")
    
    st.subheader("Integrantes do Grupo")
    integrante1, integrante2, integrante3 = st.columns(3)
    with integrante1:
        st.subheader("Beatriz Muniz")
        st.write("SP3161315")

    with integrante2:
        st.subheader("Felipe Teixeira")
        st.write("SP3155048")

    with integrante3:
        st.subheader("João Pedro")
        st.markdown("SP3137627")

    st.subheader("Instituto Federal de Ciência e Tecnologia de São Paulo")

with st.container():
    st.header("Resumo", divider=True)

    st.markdown("""
        <div style="text-align: justify;">
        Este trabalho apresenta uma análise exploratória de dados sobre a criminalidade na cidade de Los Angeles, utilizando três conjuntos de dados distintos que abrangem dados de crimes cometidos de 2020 até o presente, ligações para polícia em 2022 e dados de prisões de 2020 até o presente. O objetivo principal do estudo é identificar padrões, tendências e relações nos registros criminais, transformando dados brutos em informações estratégicas. Para isso, o projeto foi estruturado para responder questões desenvolvidas durante a análise exploratória dos dados. A metodologia aplicada envolveu técnicas de estatística descritiva para sumarizar as variáveis, o cálculo de probabilidades para avaliar a chance de eventos específicos, e a aplicação de inferência estatística, incluindo testes de hipótese para validar correlações entre as bases de dados. O estudo conclui que a análise integrada dos dados oferece uma compreensão aprofundada da dinâmica criminal em Los Angeles, fornecendo insights valiosos que podem auxiliar na formulação de políticas de segurança pública mais eficazes.
        </div>
    """, unsafe_allow_html=True)

with st.container():
    st.header("Sumário", divider=True)

    st.markdown("- **[Resumo](#resumo)**")
    st.markdown("- **[Sumário](#sumario)**")
    st.markdown("- **[Introdução](#introducao)**")
    st.markdown("- **[Análise de Dados e Resultados](#analise_e_resultados)**")

with st.container():
    st.header("Introdução", divider=True, anchor='introducao')

    st.markdown("""
        <div style="text-align:justify;">
            <p>
                A segurança pública é um dos pilares para o desenvolvimento e bem-estar de grandes centros urbanos. A cidade de Los Angeles, como uma das metrópoles mais dinâmicas do mundo, enfrenta desafios complexos relacionados à criminalidade. Nesse contexto, a análise de dados se torna uma ferramenta indispensável, permitindo transformar vastos registros de ocorrências em conhecimento estratégico. Ao investigar padrões, identificar tendências e compreender as dinâmicas do crime, é possível fornecer subsídios para a otimização de recursos e o desenvolvimento de políticas de segurança mais eficazes e proativas.
            </p>
            <p>
                Este projeto se propõe a realizar uma análise exploratória e inferencial sobre a criminalidade em Los Angeles, utilizando três conjuntos de dados distintos que, juntos, oferecem uma visão multifacetada do problema. O trabalho não busca apenas descrever os dados, mas também fazer questionamentos e extrair insights a partir da intersecção das informações disponíveis.
            </p>
        </div>
    """, unsafe_allow_html=True)

with st.container():
    st.header("Análise de Dados e Resultados", divider=True, anchor='analise_e_resultados')

    st.markdown("""
        <div style="text-align:justify;">
            <p>
                Esta seção constitui o núcleo deste relatório, onde apresentamos os resultados detalhados da investigação sobre os dados de criminalidade em Los Angeles. Para garantir uma análise aprofundada e abrangente, a equipe adotou uma metodologia de trabalho dividida: cada integrante ficou responsável pela análise primária de um dos três conjuntos de dados. Essa abordagem permitiu uma imersão completa nas particularidades de cada base, resultando em uma compreensão mais rica e detalhada de suas variáveis e padrões.
            </p>
            </p>
            <p>
                Apesar da análise inicial ter sido individualizada por base de dados, a estrutura metodológica aplicada a cada uma delas foi padronizada para garantir a coesão e a  possível comparabilidade dos resultados. Conforme as instruções do projeto, cada análise foi segmentada nos três tópicos apresentados na disciplina:
            </p>
            <p>
                Estatística Descritiva: Utilizada para sumarizar e visualizar as principais características dos dados, identificando as primeiras tendências, distribuições e padrões de ocorrência.
            </p>
            <p>
                Análise de Probabilidade: Aplicada para quantificar a chance de eventos específicos, explorando as relações de dependência entre variáveis, como a probabilidade de um crime ocorrer em um determinado local ou período.
            </p>
            <p>
                Inferência Estatística: Empregada para fazer afirmações sobre a população a partir das amostras de dados, utilizando testes de hipótese para validar correlações e diferenças significativas, sendo este o ponto crucial para cruzar informações entre as diferentes bases de dados.
            </p>
            <p>
                Nos links abaixo, serão apresentados as principais análises de cada uma das bases utilizadas no projeto, contendo dentro delas suas respectivas discussões e conclusões desenvolvidas no decorrer do projeto.
            </p>
        </div>
    """, unsafe_allow_html=True)
    st.markdown("- [Análise da Base de Chamadas de 2020 até o presente](/Análises_Chamadas)")
    st.markdown("- [Análise da Base de Crimes de 2020 até o presente](/Análises_Crimes)")
    st.markdown("- [Análise da Base de Prisões de 2020 até o presente](/Análises_Prisões)")
