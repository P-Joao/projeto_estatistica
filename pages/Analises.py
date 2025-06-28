import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Análises Realizadas",
    page_icon=":material/edit_note:",
)

st.title("Análises Realizadas")

st.header("Base de prisões de 2020 para o presente")
df_arrest_data = pd.read_csv('mock_data\Arrest_Data_from_2020_to_Present.csv')

st.header(f"Colunas")


st.write(f"Quantidade de registros: ", len(df_arrest_data))

st.header("Características dos suspeitos presos")
df_suspeitos = df_arrest_data[['Age', 'Sex Code', 'Descent Code']]

st.write('Realizar testes de hipotese para verificar se diferença de proporção entre descendencias')

st.write(df_suspeitos)
colAge, colSex, colDescent = st.columns(3)
colAge.write(df_suspeitos['Age'].describe())
colSex.write(df_suspeitos['Sex Code'].describe())
colDescent.write(df_suspeitos['Descent Code'].describe())

st.write('''
    Abaixo de 10 anos não há registros de "crime" na descrição, ou são "não criminais" ou nulos.
    Alguns podem ser registros errados. 
''')
df_menores_10 = df_arrest_data[['Age', 'Charge Group Description']].loc[df_arrest_data['Age'] < 10].drop_duplicates()
df_menores_10



df_arrest_data