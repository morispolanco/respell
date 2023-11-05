import streamlit as st
import requests
import json

# Define la función para llamar a la API de Respell.ai
def call_respell_api():
    api_url = "https://api.respell.ai/v1/run"
    headers = {
        "Authorization": "Bearer 260cee54-6d54-48ba-92e8-bf641b5f4805",
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    input_data = {
        "spellId": "RP0oSnJvS2ONDeTPCOBPZ",
        "spellVersionId": "pzXV2-bDEyJAo52mtgKmS",
        "inputs": {
            "pregunta": st.text_input("Pregunta", "Example text"),
            "pais": st.text_input("Pais", "Example text"),
            "idioma": st.text_input("Idioma", "Example text"),
            
            
        }
    }
    
    response = requests.post(api_url, headers=headers, data=json.dumps(input_data))
    return response.json()

# Crear la aplicación Streamlit
st.title("Aplicación Respell.ai")

# Llamada a la API y mostrar resultados
if st.button("Ejecutar Respell.ai"):
    result = call_respell_api()
    st.json(result)
