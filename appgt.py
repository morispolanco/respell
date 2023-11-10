import streamlit as st
import requests
import json

# Configura el título de la página en el navegador
st.set_page_config(page_title="Buscador", page_icon="📚")

# Título de la aplicación
st.title("Buscador")
st.markdown("Esta aplicación responde preguntas sobre la legislación de Guatemala, buscando en la Web.")
st.text("Por Moris Polanco")

# Campo de entrada para la pregunta o caso
pregunta = st.text_area("Pregunta o caso")

# Accede al secreto de la clave de la API
api_key = st.secrets["respell_api_key"]

# Botón para obtener la respuesta
if st.button("Obtener Respuesta"):
    if not pregunta:
        st.warning("Por favor, escriba una pregunta o caso.")
    else:
        # Realizar la solicitud a la API de Respell.ai usando el secreto
        response = requests.post(
            "https://api.respell.ai/v1/run",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "spellId": "k0GhQkJOn7IKEY-BdghY6",
                "inputs": {
                    "pregunta": pregunta
                }
            })
        )
        
        # Procesar la respuesta de la API
        if response.status_code == 200:
            respuesta = response.json().get("outputs", {}).get("respuesta", "No se pudo obtener una respuesta")
            st.write("Respuesta:", respuesta)
        else:
            st.error("Error al enviar la solicitud a la API")
