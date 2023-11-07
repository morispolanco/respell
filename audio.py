import requests
import json
import streamlit as st

# Configurar la clave de API de Respell.ai
api_key = st.text_input("Respell.ai API Key", type="password")

st.title("📝 Respuesta de Respell.ai")

# Obtener entrada del usuario
pregunta = st.text_input("Pregunta")
idioma = st.text_input("Idioma")
pais = st.text_input("País")

# Realizar la solicitud a la API de Respell.ai
if api_key:
    response = requests.post(
        "https://api.respell.ai/v1/run",
        headers={
            "Authorization": f"Bearer {api_key}",
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
