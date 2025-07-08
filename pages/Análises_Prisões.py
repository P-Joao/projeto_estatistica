import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import folium
from folium.plugins import HeatMap
from streamlit_folium import folium_static


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
    fig, ax = plt.subplots()
    # Use o Seaborn para desenhar o boxplot NO EIXO (ax) que criamos.
    sns.barplot(x=df_arrest_data['Time'], ax=ax)
    # Configure os títulos e rótulos USANDO o objeto 'ax'.
    ax.set_title('Distribuição do horário de ocorrência das prisões')
    ax.set_ylabel('Número de Ocorrências')
    ax.set_xlabel('Faixa de Horário')
    ax.grid(axis='y', linestyle='--', alpha=0.7) # Adiciona uma grade para melhor leitura
    # Use st.pyplot() para renderizar a FIGURA no Streamlit.
    st.pyplot(fig)

st.header("Análise de dados de localização", divider=True)
    
with st.container(border=True):
    st.header('Análise Geográfica de Crimes :material/map:')
    st.markdown('<h4>Mapa de calor de ocorrência de crimes</h4>', unsafe_allow_html=True)
    show_map_arrest()