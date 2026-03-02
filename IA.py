import streamlit as st
from openai import OpenAI
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
modelo = OpenAI(api_key="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")

st.write("### Capivara Maluca 🦫") # markdown

#lista_mensagem as lm

if not "lm" in st.session_state:
    st.session_state["lm"] = []

for mensagem in st.session_state["lm"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

msg_user = st.chat_input("Escreva sua mensagem aqui")

if msg_user:
    st.chat_message("user").write(msg_user)
    mensagem = {"role": "user", "content": msg_user}
    st.session_state["lm"].append(mensagem)

    bdghrtehgrgertgher
