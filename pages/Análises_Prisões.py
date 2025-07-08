import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static
from scipy.stats import ttest_ind  


def create_map_arrest():
    if 'map' not in st.session_state or st.session_state.map is None:
        df_coordenadas = df_arrest_data[['LAT', 'LON']]
        df_coordenadas.dropna()
        # Selecionando apenas as coordenadas que não são outliers em LAT ou LON
        df_coordenadas = df_coordenadas[
            (np.abs(stats.zscore(df_coordenadas['LAT'])) < 3) & 
            (np.abs(stats.zscore(df_coordenadas['LON'])) < 3)
        ] 
        mapa = folium.Map(location=[34.0522, -118.2437], zoom_start=10)
        coordenadas = df_coordenadas[['LAT', 'LON']]
        coordenadas = coordenadas.to_dict()
        latitudes = coordenadas['LAT']
        longitude = coordenadas['LON']
        heat_data = list(zip(latitudes.values(), longitude.values()))
        mapa_calor = HeatMap(heat_data, radius=8, blur=12)
        mapa.add_child(mapa_calor)
        st.session_state.map = mapa  # Save the map in the session state
    return st.session_state.map

def show_map_arrest():
    m = create_map_arrest()  # Get or create the map
    folium_static(m)

@st.cache_data
def read_data_arrest():
    df_data = pd.read_csv('mock_data/Arrest_Data_from_2020_to_Present.csv')
    return df_data

def test_t_hora_sexo(df):
    """
    Realiza um teste t para verificar se há diferença significativa
    no horário médio de prisão entre homens e mulheres.
    """
    # Removendo linhas onde 'Time' ou 'Sex Code' são nulos
    df_clean = df.dropna(subset=['Time', 'Sex Code'])

    # Filtrando DataFrame para incluir apenas 'M' (Masculino) e 'F' (Feminino)
    df_filtered = df_clean[df_clean['Sex Code'].isin(['M', 'F'])]

    # Separando os dados em duas amostras
    # Amostra 1: Horários de prisão para homens
    horarios_homens = df_filtered[df_filtered['Sex Code'] == 'M']['Time']

    # Amostra 2: Horários de prisão para mulheres
    horarios_mulheres = df_filtered[df_filtered['Sex Code'] == 'F']['Time']

    st.write(f"Analisando {len(horarios_homens)} prisões de homens e {len(horarios_mulheres)} prisões de mulheres.")
    st.write("-" * 50)

    # Realizando o Teste T para Amostras Independentes
    # A função ttest_ind calcula o teste t
    stat, p_value = ttest_ind(horarios_homens, horarios_mulheres, equal_var=False) # Usamos equal_var=False pois os tamanhos das amostras são muito diferentes

    # Apresentando e Interpretando os Resultados
    st.write(f"Estatística do Teste (t-statistic): {stat:.4f}")
    st.write(f"Valor-p (p-value): {p_value:.4f}")
    st.write("-" * 50)

    # Definimos nosso nível de significância (alfa)
    alfa = 0.05

    if p_value < alfa:
        st.write(f"Conclusão: Como o valor-p ({p_value:.4f}) é menor que {alfa}, rejeitamos a hipótese nula.")
        st.write("Há uma diferença estatisticamente significativa no horário médio de prisão entre homens e mulheres.")
    else:
        st.write(f"Conclusão: Como o valor-p ({p_value:.4f}) é maior ou igual a {alfa}, não podemos rejeitar a hipótese nula.")
        st.write("Não há evidências de uma diferença estatisticamente significativa no horário médio de prisão entre homens e mulheres.")

st.set_page_config(
    page_title="Análises Realizadas",
    page_icon=":material/edit_note:",
)

st.title("Análises Realizadas")

# st.image("imgs/crisp_dm_process.png", caption="Processo de análise de dados CRISP-DM")

st.header("Base de prisões de 2020 para o presente", divider=True, anchor='analise_base_prisoes')
df_arrest_data = read_data_arrest()

st.header("Metadados da base")
df_arrest_metadados = pd.read_csv('mock_data/metadados_arrest_data.csv')
df_arrest_metadados

st.header("Base completa")
df_arrest_data

st.write(f"Quantidade de registros: ", len(df_arrest_data))

# -------------------------------------------------------------------- #
# -------------------------------------------------------------------- #
# -------------------------------------------------------------------- #

st.header("Características dos suspeitos presos", divider=True)
df_suspeitos = df_arrest_data[['Age', 'Sex Code', 'Descent Code']]

st.markdown("""
    <div style="text-align:justify;">
        Afim de entender melhor caracteristicas relacionadas aos suspeitos presos registrados na base de dados, abaixo foram realizadas análises quanto as variáveis: idade, sexo e descendência.
    </div>
""", unsafe_allow_html=True)

st.write(df_suspeitos)

with st.container(border=True):
    st.header('Análise por Idade :material/cake:')
    
    st.markdown('<h4>BoxPlot Idade</h4>', unsafe_allow_html=True)
    col1_age, col2_age = st.columns(2)
    with col1_age:
        st.write(df_suspeitos['Age'].describe())
    with col2_age:
        # Crie uma figura e um eixo com Matplotlib. 
        # Isso nos dá controle total sobre o gráfico.
        fig, ax = plt.subplots()
        # Use o Seaborn para desenhar o boxplot NO EIXO (ax) que criamos.
        sns.boxplot(y=df_suspeitos['Age'], ax=ax)
        # Configure os títulos e rótulos USANDO o objeto 'ax'.
        ax.set_title('Boxplot da Distribuição de Idades')
        ax.set_ylabel('Idade dos Suspeitos')
        ax.grid(axis='y', linestyle='--', alpha=0.7) # Adiciona uma grade para melhor leitura
        # Use st.pyplot() para renderizar a FIGURA no Streamlit.
        st.pyplot(fig)
        
    st.markdown('<h4>Distribuição de Idade</h4>', unsafe_allow_html=True)
    fig, ax = plt.subplots()
    # Use o Seaborn para desenhar o boxplot NO EIXO (ax) que criamos.
    sns.histplot(x=df_suspeitos['Age'], ax=ax, binwidth=5)
    # Configure os títulos e rótulos USANDO o objeto 'ax'.
    ax.set_title('Distribuição de Idades em Faixas de 5 Anos')
    ax.set_ylabel('Número de Indivíduos (Contagem)')
    ax.set_xlabel('Faixa Etária')
    ax.grid(axis='y', linestyle='--', alpha=0.7) # Adiciona uma grade para melhor leitura
    # Use st.pyplot() para renderizar a FIGURA no Streamlit.
    st.pyplot(fig)

    st.markdown('''
        <div style="text-align:justify;">
            A partir da análise dos gráficos de distribuição e boxplot de idade, foi possível verificar que a maior quantidade de suspeitos presos fica entre os 20 e 45 anos. Dessa forma, foi dispertada a curiosidade de verificar os outliers, abaixo do limite inferior, para isso foi filtrado do dataframe original os suspeitos presos com idade menor que 10 anos, agrupados por idade e descrição do crime cometido, gerando o dataframe abaixo:
        </div>
    ''', unsafe_allow_html=True)
    df_menores_10 = df_arrest_data.loc[df_arrest_data['Age'] <= 9].groupby(['Age', 'Charge Group Description']).size().reset_index(name='Contagem')
    df_menores_10

with st.container(border=True):
    st.header('Sexo :material/wc:')
    col1_sex, col2_sex = st.columns(2)
    with col1_sex:
        st.write(df_suspeitos['Sex Code'].describe())
    with col2_sex:
        freq_rel_m = len(df_suspeitos['Sex Code'].loc[df_suspeitos['Sex Code'] == 'M'])/len(df_suspeitos['Sex Code'])*100
        freq_rel_f = len(df_suspeitos['Sex Code'].loc[df_suspeitos['Sex Code'] == 'F'])/len(df_suspeitos['Sex Code'])*100
        st.write(f':material/male:Masculino: {freq_rel_m:.2f}%')
        st.write(f':material/female:Feminino: {freq_rel_f:.2f}%')
    

with st.container(border=True):
    st.header('Descendência :material/water_drop:')
    col1_desc, col2_desc = st.columns(2)
    with col1_desc:
        st.write(df_suspeitos['Descent Code'].describe())
    with col2_desc:
        freq_rel_desc_outros = 0
        for desc in df_suspeitos['Descent Code'].unique():
            freq_rel_desc = len(df_suspeitos['Descent Code'].loc[df_suspeitos['Descent Code'] == desc])/len(df_suspeitos['Descent Code'])*100
            if freq_rel_desc > 1 and desc!='O':
                st.write(f'{desc}: {freq_rel_desc:.2f}%')
            else:
                freq_rel_desc_outros += freq_rel_desc
        st.write(f'Outras: {freq_rel_desc_outros:.2f}%')

st.markdown('''
        <div style="text-align:justify;">
            Após verificar as porcentagem de sexo e descendência ou "blood" como é chamado nos Estados Unidos, por considerarem a etnia de uma forma diferente de como consideramos, podemos verificar que cerca de 80% dos suspeitos presos são homens, enquanto apenas 20% mulheres. Além disso, mais da metade dos suspeitos presos registrados na base (~52%) são "H" (hispânicos, latinos e mexicanos), ~27% "B" (negros) e ~16% "W" (brancos) de acordo com os metadados da base. A partir dessa análise foi buscado uma base com dados demográficos de Los Angeles, a fim de verificar se a porcentagem de cada uma das etnias dos suspeitos presos seria proporcional ou não a população, mas devido a não ter sido encontrada uma base confiável com esses dados, não foi possível realizar esse teste. 
        </div>
    ''', unsafe_allow_html=True)

# -------------------------------------------------------------------- #
# -------------------------------------------------------------------- #
# -------------------------------------------------------------------- #

st.header("Análise de dados relacionados as prisões", divider=True)

with st.container(border=True):
    st.header('Horário de Ocorrência das Prisões :material/alarm:')

    df_crimes_horario = df_arrest_data.groupby(['Time']).size().reset_index(name='Contagem')
    df_crimes_horario['Time'] = df_crimes_horario['Time'].astype(int)
    df_crimes_horario['Hora'] = (df_crimes_horario['Time'] - 1) // 100
    df_crimes_horario_hora = df_crimes_horario[['Hora','Contagem']].groupby(['Hora']).sum().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(
        data=df_crimes_horario_hora,
        x='Hora',
        y='Contagem',
        ax=ax,
        palette='viridis'
    )
    ax.set_title('Contagem de Prisões por Hora do Dia')
    ax.set_xlabel('Hora do Dia (00h - 23h)')
    ax.set_ylabel('Número de Prisões')
    st.pyplot(fig)

    st.markdown('''
        <div style="text-align: justify;">
            <p>
                Após a análise da base do gráfico prisões por hora, fica visível que a maior quantidade de prisões fica das 14h às 22h e também é possível visualizar que após o começo da madrugada (23h - 00h) a quantidade de prisões começa a decair gradativamente até as 5h onde é localizado o menor ponto de contagem de prisões da base.
            </p>
            <p>
                A partir da informação visualizada no gráfico também foi levantada a hipótese de que a média de horário de prisão dos homens poderia ser diferente da média do horário de prisão das mulheres. Dessa forma o teste foi definido da seguinte forma:
            </p>
            <p>Hipótese Nula: Média de horário das prisões dos homens é <b>igual</b> a média de horário das prisões das mulheres.</p>
            <p>Hipótese Nula: Média de horário das prisões dos homens é <b>diferente</b> a média de horário das prisões das mulheres.</p>
            <p>Afim de realizar a verificação da hipótese, foi utilizado um teste t com nível de confiança alfa de 0.05, realizado da seguinte forma:</p>
        </div>
    ''', unsafe_allow_html=True)
    st.code('''
        from scipy.stats import ttest_ind
            
        """
        Realiza um teste t para verificar se há diferença significativa
        no horário médio de prisão entre homens e mulheres.
        """
        # Removendo linhas onde 'Time' ou 'Sex Code' são nulos
        df_clean = df_arrest_data.dropna(subset=['Time', 'Sex Code'])

        # Filtrando DataFrame para incluir apenas 'M' (Masculino) e 'F' (Feminino)
        df_filtered = df_clean[df_clean['Sex Code'].isin(['M', 'F'])]

        # Separando os dados em duas amostras
        # Amostra 1: Horários de prisão para homens
        horarios_homens = df_filtered[df_filtered['Sex Code'] == 'M']['Time']

        # Amostra 2: Horários de prisão para mulheres
        horarios_mulheres = df_filtered[df_filtered['Sex Code'] == 'F']['Time']

        print(f"Analisando {len(horarios_homens)} prisões de homens e {len(horarios_mulheres)} prisões de mulheres.")
        print("-" * 50)

        # Realizando o Teste T para Amostras Independentes
        # A função ttest_ind calcula o teste t
        stat, p_value = ttest_ind(horarios_homens, horarios_mulheres, equal_var=False) # Usamos equal_var=False pois os tamanhos das amostras são muito diferentes

        # Apresentando e Interpretando os Resultados
        print(f"Estatística do Teste (t-statistic): {stat:.4f}")
        print(f"Valor-p (p-value): {p_value:.4f}")
        print("-" * 50)

        # Definimos nosso nível de significância (alfa)
        alfa = 0.05

        if p_value < alfa:
            print(f"Conclusão: Como o valor-p ({p_value:.4f}) é menor que {alfa}, rejeitamos a hipótese nula.")
            print("Há uma diferença estatisticamente significativa no horário médio de prisão entre homens e mulheres.")
        else:
            print(f"Conclusão: Como o valor-p ({p_value:.4f}) é maior ou igual a {alfa}, não podemos rejeitar a hipótese nula.")
            print("Não há evidências de uma diferença estatisticamente significativa no horário médio de prisão entre homens e mulheres.")
    ''', language='python')
    st.markdown('''
        <div style="text-align: justify;">
            <p>
                Assim após a execução do código acima obtivemos o seguinte resultado:
            </p>
        </div>
    ''', unsafe_allow_html=True)

    test_t_hora_sexo(df_arrest_data)


st.header("Análise de dados de localização", divider=True)
    
with st.container(border=True):
    st.header('Análise Geográfica de Crimes :material/map:')
    st.markdown('<h4>Mapa de calor de ocorrência de crimes</h4>', unsafe_allow_html=True)
    show_map_arrest()