import streamlit as st
from agent import orquestador
import os

# Ruta del dataset
file_path = "./data/M03_01_La_Paz.csv"

# Configuración de la página
st.set_page_config(page_title="Agente de Datos CSV", page_icon="🤖", layout="centered")
st.title("Chat con Agente de Datos (Ollama + Pandas)")

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant" and msg.get("image"):
            st.image(msg["image"])
        else:
            st.markdown(msg["content"])

# Input del usuario
user_input = st.chat_input("Escribe una pregunta sobre el CSV...")

if user_input:
    # Mostrar pregunta en pantalla
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Procesar pregunta con el agente
    with st.spinner("Analizando..."):
        response = orquestador(user_input, file_path)

    # Si la respuesta es una ruta de imagen → mostrar la gráfica
    if isinstance(response, str) and response.endswith(".png") and os.path.exists(response):
        st.chat_message("assistant").image(response)
        st.session_state.messages.append({"role": "assistant", "image": response})
    else:
        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
