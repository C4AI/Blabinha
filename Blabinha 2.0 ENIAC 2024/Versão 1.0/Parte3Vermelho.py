import os
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path
import FileManipulator as manip

stars = 0

cara = []

load_dotenv()

client = OpenAI(
    # api_key defaults to os.environ.get("openai_API_KEY")  
    api_key=os.getenv("OPENAI_API_KEY"),

)
modeloGPT =  "gpt-4-turbo"
def enviaResultados(respostas):
    #Inicio as duas variaveis
    falaGPT_total = ""

    #Recebo as respostas do GPT e formato os valores
    for r in respostas:
        falaGPT = r.choices[0].message.content
        falaGPT = falaGPT.replace(".", ".\n")
        falaGPT_total = falaGPT_total + "||" + falaGPT


    #Retorno a resposta do GPT formatada
    return falaGPT_total

def escreveFalas(texto):
    print("###############################################################")
    print(texto)
    print("###############################################################")

def geraTopicos(file_path):
        
    textos = returnFalasResposta(file_path)

    topicos = ["Meio Ambiente","Governança","Riquezas"]

    lista = []

    for t in textos:
        for x in topicos:         
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content": t[0]},
                    {"role": "assistant", "content": t[1]},
                    {"role": "system", "content": "Leia a conversa e veja se ela está relacionada ao tópico " + x + "Para gerar a saida retorne TRUE se estiver relacionado e FALSE se não tiver"},
                ]
            )
            if (response.choices[0].message.content == "TRUE"):
                lista.append(x)
    contagem = []

    for x in topicos:
        contagem.append(str(lista.count(x)) + "vezes do tópico:" + str(x))

    if(len(lista) >=14):
        contagem.append(4)
    elif(len(lista) >= 10):
        contagem.append(3)
    elif(len(lista) >= 7):
        contagem.append(2)
    else:
        contagem.append(1)


    return contagem

def analisaRespostas(file_path):
    falas = manip.returnQuests(file_path)
    #lista = []
    #if len(falas) == 0:
    #    lista.append(0)
    #    lista.append(0)
    #    return lista 
    #lista.append(len(falas))
    #lista.append(0)
    #for t in falas:
    #    print(t)        
    #    response = client.chat.completions.create(
    #        model=modeloGPT,
    #        messages=[
    #            {"role": "user", "content": t['falaUser']},
    #           {"role": "assistant", "content": t['falaGPT']},
    #            {"role": "system", "content":"Leia a conversa e veja se o usuario respondeu corretamente conforme o que foi dito pelo assistente." +
    #             " Para gerar a saida retorne TRUE se o usuario tiver respondido corretamente e FALSE se não tiver "},
    #        ]
    #    )
    #    if (response.choices[0].message.content.__contains__("TRUE")):
    #        print()
    #        print()
    #        print("Aumentou em 1")
    #        lista[1] = lista[1] + 1

    return len(falas)

#Retorna a quantidade de estrelas por completude de interação
def estrelasCompletude(file_path):
    '''
    Recebe a conversa que a pessoa teve e verifica o quanto ela interagiu
    :param str file_path: caminho para o arquivo da conversa
    :retun: quantidade de estrelas
    :rtype: int
    '''

    parte2 = manip.readJson(file_path)
    var = 0
    for p in parte2:
        if( (p['secao'] < 240) and (p['secao'] > var) ):
            var = p['secao']
    if(var >= 216):
        return 4
    if(var >= 215):
        return 3
    if(var >= 213):
        return 2
    if(var >= 211):
        return 1
    return 0 

#Agrupa falas e resposta da parte 02
def agrupaFalasResposta(data):
    dict_dialogues = {}

    for pergunta, resposta in data:
        if pergunta not in dict_dialogues:
            dict_dialogues[pergunta] = []
        dict_dialogues[pergunta].append(resposta)

    lista_agrupada = [(pergunta, '\n'.join(respostas)) for pergunta, respostas in dict_dialogues.items()]
    return lista_agrupada  

#Retorna as falas e respostas agrupadas da parte02
def returnFalasResposta(file_path):
    user = []
    blabinha = []
    parte2 = manip.returnParte2(file_path)
    for p in parte2:
        user.append(p['falaUser'])
        blabinha.append(p['falaGPT'])
    data = list(zip(user, blabinha))

    lista_agrupada = agrupaFalasResposta(data)
    
    return lista_agrupada

def escolheQuestões(tamanho):
    '''
    Retorna onde ir conforme a quantidade de questões respondidass
    :param int tamanho: tamanho das questões
    :return: valor da secao
    :rtype: int
    '''
    if(tamanho > 2):
        return 324
    if(tamanho > 1):
        return 323
    return 322
#Gera o texto perguntando as opções de resposta do usuario para parte 03
def promptQuestões(perguntas):
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
            {"role": "system", "content": "Siga os passos a seguir para gerar a saida:" +
            "1 - Diga que como a pessoa respondeu corretamente "+ str(len(perguntas)) +" perguntas e que por isso ela ganhou" + str(len(perguntas)) + "estrelas . 2 - E que agora ela podera escolher algumas coisas do super-héroi" +
            "3 Terminando perguntado o que ela vai escolher. as perguntas são" + str(perguntas) },
        ]
    )
    return response

def verificaBonus(bonus):
    response = client.chat.completions.create(
    model=modeloGPT,
    messages=[
        {"role": "user", "content": bonus['falaUser']},
        {"role": "assistant", "content": bonus['falaGPT']},
        {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
        {"role": "system", "content": "Verifique qual ferramenta a pessoa escolheu. E retorne somente o qual é a ferramenta. Exemplo de saida: 'Tridente Mágico', 'Escudo protetor'" },

        ]
    )

    return response.choices[0].message.content


