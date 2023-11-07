import streamlit as st
import requests
import json

# Configura el título de la página en el navegador
st.set_page_config(page_title="LeybotGt", page_icon="📚")

# Título de la aplicación
st.title("LeybotGt")
st.markdown("Esta aplicación responde preguntas relacionadas con la legislación de Guatemala.")
st.text("Por Moris Polanco")

# Campo de entrada para la pregunta o caso
pregunta = st.text_area("Pregunta o caso")

# Botón para obtener la respuesta
if st.button("Obtener Respuesta"):
    if not pregunta:
        st.warning("Por favor, escriba una pregunta o caso.")
    else:
        # Realizar la solicitud a la API de Respell.ai
        response = requests.post(
            "https://api.respell.ai/v1/run",
            headers={
                "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "spellId": "k0GhQkJOn7IKEY-BdghY6",
                "spellVersionId": "4_nhg1PEL1GaU1IUsVWAT",
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
