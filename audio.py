import streamlit as st
import sounddevice as sd

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
    # Resto de tu código para obtener la respuesta de la API con la pregunta

# Botón para capturar audio en vivo
    if st.button("Capturar Audio en Vivo"):
        st.warning("Habilitando captura de audio en vivo... Presiona el botón de detener cuando hayas terminado.")
        
        audio_stream = st.empty()
        
        # Configura la captura de audio en vivo
        sample_rate = 44100
        duration = 10  # Duración en segundos
        audio_data = sd.rec(int(sample_rate * duration), samplerate=sample_rate, channels=1, dtype='int16')
        sd.wait()  # Espera a que termine la captura
    
    # Puedes procesar audio_data como desees (por ejemplo, enviarlo a una API para análisis)

# Resto de tu código

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

# Botón para procesar audio en vivo
if st.button("Audio en Vivo"):
    st.warning("Habilitando audio en vivo... Presiona el botón de detener cuando hayas terminado.")
    
    audio_stream = st.empty()
    p = pyaudio.PyAudio()
    
    # Configura los parámetros de audio, como la tasa de muestreo y la duración
    sample_rate = 44100
    duration = 10  # Duración en segundos
    
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=1024)
    
    audio_data = []

    while True:
        try:
            audio_chunk = np.frombuffer(stream.read(1024), dtype=np.int16)
            audio_data.append(audio_chunk)
            audio_stream.audio(audio_chunk)
        except KeyboardInterrupt:
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Procesar audio_data como desees (por ejemplo, enviarlo a una API para análisis)
