import streamlit as st
from openai import OpenAI
import BlabGPTAzul as gera
import time
import tempfile
import json


def main():     

    st.header("Visualizador de :orange[log]")

    files_bruto = st.sidebar.file_uploader("Abra o log na forma :orange[JSON]",accept_multiple_files=True)
    files_chat = st.sidebar.file_uploader("Abra o log na forma :orange[CHAT]",accept_multiple_files=True)

    def retornaJson(files):
        lista = []
        for f in files:
            arquivo = f.read().decode('utf-8')
            lista.append(json.loads(arquivo))
        return lista

    conta  = st.container(border = True, height= 500)    

    if files_bruto:
        lista = retornaJson(files_bruto)
        with conta:
            st.subheader("Testador: :orange[" + str(lista[0]['Nome']) + "]")            
            for l in lista:
                st.write(l)

    if files_chat:
        listas = retornaJson(files_chat)
        with conta:
            st.subheader("Testador: :orange[" + str(listas[0]['Nome']) + "]")            
            for l in listas:
                with st.chat_message("user"):
                    st.write(l['falaUser'])
                with st.chat_message("assistant"):
                    st.write(l['falaGPT'].replace("//",""))




if __name__ == "__main__":
    main()