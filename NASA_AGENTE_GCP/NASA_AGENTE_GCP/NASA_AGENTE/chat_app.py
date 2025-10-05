import streamlit as st
from agent_gcp_vertex import orquestador
import os
import time

# Ruta del dataset
file_path = "./data/M03_01_La_Paz.csv"

# Configuración de la página
st.set_page_config(page_title="Agente de Datos CSV", page_icon="🤖", layout="centered")
st.title("🤖 Chat con Agente de Datos (Gemini - Vertex AI + Pandas)")

# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar historial anterior
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant" and msg.get("image"):
            st.image(msg["image"], use_container_width=True)
        else:
            st.markdown(msg["content"])

# Entrada del usuario
user_input = st.chat_input("Escribe una pregunta sobre el CSV...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("🔎 Analizando datos con Gemini..."):
        start_time = time.time()
        try:
            response = orquestador(user_input, file_path)
        except Exception as e:
            response = f"⚠️ Error al procesar la solicitud: {e}"

        elapsed = time.time() - start_time

    # Mostrar respuesta
    if isinstance(response, str) and response.endswith(".png") and os.path.exists(response):
        st.chat_message("assistant").image(response, use_container_width=True)
        st.session_state.messages.append({"role": "assistant", "image": response})
        st.success(f"Gráfica generada correctamente. ⏱️ {elapsed:.1f}s")
    else:
        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.caption(f"⏱️ Respuesta en {elapsed:.1f} segundos")