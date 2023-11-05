import streamlit as st
import requests
import json

# Título de la aplicación
st.title("Preguntas legales")

# Campos de entrada para el usuario
pregunta = st.text_input("Pregunta", "Escribe tu pregunta aquí")
pais = st.text_input("País", "Escribe tu país aquí")
idioma = st.text_input("Idioma", "Escribe tu idioma aquí")

# Botón para corregir el texto
if st.button("Corregir Texto"):
    # Realizar la solicitud a la API de Respell.ai
    response = requests.post(
        "https://api.respell.ai/v1/run",
        headers={
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
        })
    )

    # Procesar la respuesta de la API
    if response.status_code == 200:
        corrected_text = response.json().get("outputs", {}).get("pregunta", "Error al corregir el texto")
        st.write("Texto corregido:", corrected_text)
    else:
        st.write("Error al enviar la solicitud a la API")

