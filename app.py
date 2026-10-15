import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('YARDAS_PASOS_DATOS_TICS.xlsx', index_col=0)
st.title("Este es un análisis estadístico")
st.header("Base de datos de Yardas vs. Pases")
st.dataframe(df.head())

#Esta es la estadística descriptiva.
st.header("Estadística descriptiva")
st.dataframe(df.describe())

#Esto esta estandarizando las columnas.
df.columns = [c.lower().replace(' ', '_') for c in df.columns]

#Este es el diagrama de caja y bigote de Yardas totales
fig, ax = plt.subplots()
ax.boxplot(df['yardas_totales'])
st.header("Diagrama de caja y bigote de Yardas totales")
st.pyplot(fig)

#Este es el diagrama de caja y bigote de pases completos
fig, ax = plt.subplots()
ax.boxplot(df['pases_completos'])
st.header("Diagrama de caja y bigote de Pases Completos")
st.pyplot(fig)

col1, col2 = st.columns(2)

with col1:
    #Este es el diagrama de caja y bigote de Yardas totales
    fig, ax = plt.subplots()
    ax.boxplot(df['yardas_totales'])
    st.header("Diagrama de caja y bigote de Yardas totales")
    st.pyplot(fig) 

with col2:
    #Este es el diagrama de caja y bigote de pases completos
    fig, ax = plt.subplots()
    ax.boxplot(df['pases_completos'])
    st.header("Diagrama de caja y bigote de Pases Completos")
    st.pyplot(fig)

