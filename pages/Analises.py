import streamlit as st
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Análises Realizadas",
    page_icon=":material/edit_note:",
)

st.title("Análises Realizadas")

# st.image("imgs/crisp_dm_process.png", caption="Processo de análise de dados CRISP-DM")

st.header("Base de prisões de 2020 para o presente", divider=True)
df_arrest_data = pd.read_csv('mock_data\Arrest_Data_from_2020_to_Present.csv')

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

st.write('Realizar testes de hipotese para verificar se diferença de proporção entre descendencias')

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

    st.write('''
        Análise dos outliers de idade (Registros com z-score de idade > 3). 
    ''')
    df_menores_10 = df_arrest_data[['Age', 'Charge Group Description']].loc[df_arrest_data['Age'] < 9].drop_duplicates()
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