import streamlit as st
from openai import OpenAI
import BlabGPTVermelho as gera
from datetime import datetime
import time

#******** OBSERVAÇÂO ***********
# A lista chat['varial'] é utilizada para trocar informações entre a interface e o GPT
# Presta atenção o que cada posição representa
# [0] -> Status | [1] -> Fala Usuario Atual | [2] -> Fala GPT Atual  | [3] -> Quantidade de Bônus rodados | [4] -> Nome da pessoa | [5] -> Nome da Pasta Log


#Funçaõ responsavel por criar os chats 
def create_chat(chat):
    #Titulo presente em todos chats
    st.title("" +  chat['name'] + " Blabinha Versão :red[Vermelho]")
    st.header("Testador: :red[" + st.session_state["nome"]+ "]")
 

    statusGeral =  st.status("Pronto para uso", expanded=False, state="complete")
    conta  = st.container(border = True, height= 600)

    def ajustaTexto(nome):
        nome = st.session_state["nome"].replace(" ","")
        nome = nome.lower()
        return nome

    
    if "varial" not in chat:
        chat['varial'] = [100,"","",0,ajustaTexto(st.session_state['nome']), ""]
        
    #Função responsavel por gerar uma resposta referente ao que a pessoa falou  

    def generateResposta(texto):    

        chat['varial'][1] = texto
        chat['varial'][5] = st.session_state['tempo'] + str(chat['name']).replace(" ","_")         
        chat['varial'] = gera.escolheParte(chat['varial'])

        with conta:
            # Display assistant response in chat message container
            texto =  chat['varial'][2]
            texto = texto.split("||")
            for r in texto:
                if not ( r == ""):
                    with st.chat_message("assistant"):
                        st.markdown(r)
                        # Add assistant response to chat history
                        chat['messages'].append({"role": "assistant", "content":r})

        statusGeral.update(state="complete",label="Pronto para uso")

    #Cria a barra lateral contendo as informações necessarios e a opçõa de mudar de chat
    if "messages" not in chat:
        chat['messages'] = []
        
    with conta:
        for message in chat['messages']:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("Envie sua mensagem"):
        statusGeral.update(label="Processando",state="running")
        with conta:
            with st.chat_message("user"):
                st.markdown(prompt)
        chat['messages'].append({"role": "user", "content": prompt})
        generateResposta(prompt)




def main(): 
    
    #Cria e retorna os chats
    if 'chats' not in st.session_state:
        st.session_state['chats'] = [{'name': 'Chat 0', 'messages': []}]
    
    if "tempo" not in st.session_state:
        st.session_state['tempo'] = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')


    if 'nome' not in st.session_state:
        st.session_state['nome'] = "Erro nome não encontrado"   
    
    st.sidebar.subheader(":red[Interagindo:]")
    st.sidebar.write("Para interagir, basta utilizar o chat 👉")
    st.sidebar.write(" Você pode escrever o que quiser na caixa de entrada no fim da página. A Blabinha deverá responder à sua entrada.") 
    st.sidebar.divider()

    # Add new chat with a default name
    add_chat_button = st.sidebar.button(":red[Criar Novo Chat]")

    if add_chat_button:
        new_chat_name = f"Chat {len(st.session_state['chats'])}"
        st.session_state['chats'].append({'name': new_chat_name, 'messages': []})
        placeholder = st.sidebar.empty()
        with st.sidebar:
            placeholder.header("**Novo chat criado!**")
            time.sleep(1)
            placeholder.header("")


    selected_chat_index = st.sidebar.selectbox("Selecione o Chat:", range(len(st.session_state['chats'])), index=0, key="select_chat")
    

    st.sidebar.subheader(":red[Chats:]")
    st.sidebar.write("Você pode criar chats novos clicando no botão acima 👆. Depois de criar, escolha o novo chat na caixa de listagem para iniciá-lo.")
    st.sidebar.write(" Na 'caixa de listagem' abaixo estão todos os seus chats. Você pode navegar entre eles se você achar interessante para o seu teste.") 
    st.sidebar.divider()
    st.sidebar.subheader(":red[Problemas:]")
    st.sidebar.write("Se você se deparar com algum problema de cunho técnico: o chat travou, você recebeu uma mensagem de erro, ou coisa parecida, anote em qual chat isso ocorreu, o dia e horário que você está fazendo o teste e nos envie por email.") 
    st.sidebar.write("Email: teodoro538@usp.br") 
    st.sidebar.write("Não esqueça de responder a pesquisa de avaliação da Blabinha no Google Forms  https://forms.gle/zj8rgxnS4uoDAdxZ9 . A avaliação no Google Forms é APENAS sobre sua experiência no diálogo.")





    # Show the selected chat
    if st.session_state['chats']:
        create_chat(st.session_state['chats'][selected_chat_index])

if __name__ == "__main__":
    main()