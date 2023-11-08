import streamlit as st
import requests
import json

# Configura el título de la página en el navegador
st.set_page_config(page_title="LeybotGt", page_icon="📚")

# Título de la aplicación
st.title("LeybotGt")
st.markdown("Esta aplicación responde preguntas relacionadas con la legislación de Guatemala.")
st.text("Por Moris Polanco")

# Clave de API de Respell
clave_api = st.text_input("Clave de API de Respell")

# Campo de entrada para la pregunta o caso
pregunta = st.text_area("Pregunta o caso")



# Botón para obtener la respuesta
if st.button("Obtener Respuesta"):
    if not pregunta:
        st.warning("Por favor, escriba una pregunta o caso.")
    elif not clave_api:
        st.warning("Por favor, ingrese una clave de API de Respell.")
    else:
        # Realizar la solicitud a la API de Respell.ai
        response = requests.post(
            "https://api.respell.ai/v1/run",
            headers={
                "Authorization": f"Bearer {clave_api}",
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
