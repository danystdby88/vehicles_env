import streamlit as st
import pandas as pd
import plotly.express as px
import pandas as pd
df = pd.read_csv('vehicles_us.csv')
st.title('📈 Mercado de Coches Usados: Un Vistazo Rápido')

# Titulo de la aplicación
st.title('Generador de Histograma Interactivo')
st.write('Haz clic en el botón para visualizar la distribución de los datos.')

# --- El botón que activa la creación del gráfico ---
if st.button('Generar Histograma'):
    # Crear el histograma con Plotly Express
    # Se usa px.histogram() porque es más sencillo para este tipo de gráfico
    fig = px.histogram(df, x='odometer', 
                       title='Distribución de Kilometraje (Odómetro)',
                       labels={'odometer': 'Kilometraje (en km)', 'count': 'Frecuencia'})

    # Mostrar el gráfico en la aplicación de Streamlit
    st.plotly_chart(fig, use_container_width=True)
    st.write("¡El gráfico se ha generado con éxito!")


# Título de la aplicación
st.title('Generador de Gráficos con Casillas de Verificación')
st.write('Selecciona las casillas de verificación para mostrar los gráficos.')

# Asumiendo que 'df' ya está cargado con las columnas necesarias

# Casillas de verificación para cada gráfico
show_histogram = st.checkbox('Mostrar Histograma del Odómetro')
show_scatter = st.checkbox('Mostrar Gráfico de Dispersión (Precio vs. Odómetro)')

# --- Lógica para mostrar el Histograma ---
if show_histogram:
    # Crear el histograma
    fig_hist = px.histogram(df, x='odometer', 
                            title='Distribución de Kilometraje (Odómetro)',
                            labels={'odometer': 'Kilometraje del Vehículo', 'count': 'Frecuencia'})

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig_hist, use_container_width=True)
    st.write("¡El histograma se ha generado exitosamente!")

# --- Lógica para mostrar el Gráfico de Dispersión ---
if show_scatter:
    # Crear el gráfico de dispersión
    fig_scatter = px.scatter(df, x='odometer', y='price',
                             title='Relación entre Precio y Kilometraje',
                             labels={'odometer': 'Kilometraje (km)', 'price': 'Precio ($)'},
                             hover_data=['odometer', 'price'])

    # Mostrar el gráfico de dispersión en Streamlit
    st.plotly_chart(fig_scatter, use_container_width=True)
    st.write("¡El gráfico de dispersión se ha generado exitosamente!")
