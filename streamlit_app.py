import requests
import json
import streamlit as st

st.title("Aplicación con Respell.ai")

# Campos de entrada
pregunta = st.text_input("Pregunta", "Escribe tu pregunta aquí")
pais = st.text_input("País", "Escribe tu país aquí")
idioma = st.text_input("Idioma", "Escribe tu idioma aquí")

# Botón para enviar la solicitud a la API
if st.button("Enviar solicitud"):
    response = requests.post(
        "https://api.respell.ai/v1/run",
        headers={
            # Esta es tu clave API
            "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
            "Accept": "application/json",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "spellId": "RP0oSnJvS2ONDeTPCOBPZ",
            "spellVersionId": "pzXV2-bDEyJAo52mtgKmS",
            "inputs": {
                "pregunta": pregunta,
                "idioma": idioma,
                "pais": pais
            }
        }),
    )

    # Procesar la respuesta aquí

