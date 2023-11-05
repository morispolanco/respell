import streamlit as st
import requests

# Define la URL de la API y la clave de autenticación
api_url = "https://api.respell.ai/v1/run"
api_key = "260cee54-6d54-48ba-92e8-bf641b5f4805"

st.title("API Respell.ai Demo")

# Ingresa la pregunta del usuario en español
user_question = st.text_input("Ingresa tu pregunta en español")

if st.button("Obtener Respuesta"):
    # Configura los parámetros de la solicitud
    headers = {
        "authorization": f"Bearer {api_key}",
        "accept": "application/json",
        "content-type": "application/json",
    }

    payload = {
        "spellId": "RP0oSnJvS2ONDeTPCOBPZ",
        "spellVersionId": "6m89Lc40p6kW-yS82NK5H",
        "inputs": {"pregunta": user_question},
    }

    # Realiza la solicitud a la API
    response = requests.post(api_url, headers=headers, json=payload)

    if response.status_code == 200:
        # Obtiene la respuesta en formato JSON
        api_response = response.json()
        st.subheader("Respuesta:")
        st.write(api_response)

    else:
        st.error("Error al obtener datos de la API. Verifica tu configuración y vuelve a intentarlo.")
