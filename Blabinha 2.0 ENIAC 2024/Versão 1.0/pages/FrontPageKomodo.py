# Importe a biblioteca Streamlit
import streamlit as st

# Título da página
st.title(":red[Aplicação Blabinha versão Vermelho]")
st.subheader("Observação:")
st.write(":one: Nessa primeira tela você informa seu nome para que possamos fazer um controle da avaliação, para fins de análise dos logs posteriormente.")
st.write(":two: A partir da próxima tela, quando você estará interagindo com a Blabinha, ela vai novamente perguntar o seu nome. Nessa ocasião, você pode responder o que quiser (inclusive se recusar a dizer seu nome, falar um nome falso, etc).")
if 'nome' not in st.session_state:
    st.session_state['nome'] = ""   

# Adiciona um campo de entrada de texto para o nome
nome = st.text_input("Por favor, insira seu nome para iniciar e pressione 'enter'")

# Verifica se o campo de nome não está vazio
if nome:
    # Exibe uma mensagem de boas-vindas com o nome inserido
    st.session_state['nome'] = nome

    st.write(f"Olá, :red[ **{nome}**!]")

    if st.button(":red[**Clique aqui para começar**]"):
        st.switch_page("pages/Komodo.py")
