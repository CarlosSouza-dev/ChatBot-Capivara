import streamlit as st
from openai import OpenAI

modelo = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.write("### Capivara 🦫") # markdown

#lista_mensagem as lm

if not "lm" in st.session_state:
    st.session_state["lm"] = []

for mensagem in st.session_state["lm"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

msg_user = st.chat_input("Escreva sua mensagem aqui")

if msg_user:
    #msg ususario
    st.chat_message("user").write(msg_user)
    mensagem = {"role": "user", "content": msg_user}
    st.session_state["lm"].append(mensagem)

    #resposta ia
    #resposta do modelo as rm

    rm = modelo.chat.completions.create(messages=st.session_state["lm"], model="gpt-4o")

    resp_ia = rm.choices[0].message.content
    
    # exibir a resposta da IA
    st.chat_message("assistant", avatar="🦫").write(resp_ia)
    msg_ia = {"role": "assistant", "content": resp_ia}
    st.session_state["lm"].append(msg_ia)