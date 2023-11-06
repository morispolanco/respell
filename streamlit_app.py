import streamlit as st
import requests
import json

# Configura el título de la página en el navegador
st.set_page_config(page_title="Leybot", page_icon="📚")

# Accede a la clave de la API de Respell.ai desde los secrets
api_key = st.secrets["respell"]["api_key"]

# Título de la aplicación
st.title("Preguntas y casos de legislación")
st.markdown("Plantee una pregunta o un caso sobre las leyes de cualquier país.")
st.text("Por Moris Polanco")

# Campos de entrada para el usuario
pregunta = st.text_area("Pregunta o caso", "Escribe tu pregunta o plantea tu caso aquí")
pais = st.text_input("País", "Escribe tu país aquí")
idioma = st.text_input("Idioma", "Escribe tu idioma aquí")

# Botón para obtener la respuesta
if st.button("Obtener Respuesta"):
    if not pregunta or not pais or not idioma:
        st.warning("Por favor, complete todos los campos de entrada.")
    else:
        # Realizar la solicitud a la API de Respell.ai
        response = requests.post(
            "https://api.respell.ai/v1/run",
            headers={
                "Authorization": f"Bearer {api_key}",  # Utiliza la variable api_key
                "Accept": "application/json",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "spellId": "RP0oSnJvS2ONDeTPCOBPZ",
                "inputs": {
                    "pregunta": pregunta,
                    "idioma": idioma,
                    "pais": pais
                }
            })
        )
        
        # Procesar la respuesta de la API
        if response.status_code == 200:
            respuesta = response.json().get("outputs", {}).get("respuesta", "No se pudo obtener una respuesta")
            st.write("Respuesta:", respuesta)
        else:
            st.error("Error al enviar la solicitud a la API")
