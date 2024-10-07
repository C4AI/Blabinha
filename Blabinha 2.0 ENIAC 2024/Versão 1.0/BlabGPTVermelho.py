import random
import math
import os
from dotenv import load_dotenv
from openai import OpenAI
import FileManipulator as manip
import Parte3Vermelho as parte3

load_dotenv()

stat = 0

#******** OBSERVAÇÂO ***********
# A lista chat['varial'] é utilizada para trocar informações entre a interface e o GPT
# Presta atenção o que cada posição representa
# [0] -> Status | [1] -> Fala Usuario Atual | [2] -> Fala GPT Atual  | [3] -> Quantidade de Bônus rodados | [4] -> Nome da pessoa | [5] -> Nome da Pasta Log


client = OpenAI(
    # api_key defaults to os.environ.get("openai_API_KEY")  
    api_key=os.getenv("OPENAI_API_KEY"),
)

class variaveis:
    def __init__(self):
        self.estrelas = 0
        self.limite = 0
        self.hero = []
        self.path = ""

    def setPath(self,variaveis):
        '''
        seta o path da conversa atual
        '''
        self.estrelas = 0
        self.heto = []
        self.path = manip.return_dialog_folder(variaveis[4],variaveis[5])

    def pathTeste(self):
         '''
         seta um path para testar a parte03
         '''
         path_Vivan = "DiaLOGS\\vivian\\Chat_0_tempo3M_27D_16H_"
         path_Bibi = "DiaLOGS\\bibi\\2024_04_24_20_03_15Chat_0"
         self.path = path_Bibi

    def getPath(self):
        '''
        :return: Retorna o path setado anteriormente
        :rtype: string
        '''
        return self.path
    
    def addStar(self, quantidade: int):
        '''
        :param int quantidade: Adiciona a quantidade de estrelas no total
        '''
        self.estrelas = self.estrelas + quantidade


    def addHeroFeature(self, feature: str):
        '''
        :param str feature: String com a feature do herói
        '''
        self.hero.append(feature)

    def getHeroFeature(self):
        '''
        :return: texto formato com todas as features do herói
        :rtype: string
        '''
        tamanho = len(self.hero)
        frase_final = ""
        if tamanho >= 5:
            frase_final = "O herói tem uma casa: " + self.hero[4]
        if tamanho >= 4:
            frase_final =  frase_final + ". O herói tem como companheiro um :" + self.hero[3]
        if tamanho >= 3:
            frase_final =  frase_final + ". O herói tem uma capa com as seguintes características:" + self.hero[2]
        if tamanho >=2:
            frase_final = frase_final + ". A roupa do herói tem as seguintes características :" + self.hero[1]
        return (frase_final + ". O herói tem como ferramenta :" + self.hero[0])

    def addLimite(self):
        '''
        Adiciona em um o valor de limite para mesma interação
        '''
        self.limite = self.limite + 1

    def resetLimite(self):
        '''
        Reseta o limite para 0
        '''
        self.limite = 0

    def getLimite(self):
        '''
        :return: retorna o valor que está limitando a interação
        :rtype: int
        '''
        print()
        print("O valor do limite é de:" + str(self.limite))
        print()

        return self.limite
    
    def getStar(self):
        '''
        :return: retorna a qauntidade de estrelas
        :rtype: int
        '''
        return self.estrelas
    
var = variaveis()

modeloGPT = "gpt-4-turbo"

def printVerificador(tipoVerificador, caso):
    print("\n-------- Verificador: " + tipoVerificador + " -------- ")
    print("\n ##### \n" + caso + " \n #####")

def printSecao(variaveis):
    print("\n-------- " + str(variaveis[0]) + " -------- ")

#Formata a resposta do gpt, envia para criação de logs e retorna a resposta formatada
def enviaResultados(respostas, variaveis):
    '''
    Formata as respostas geradas para um padrão e gera chama a função de log
    :param list variaveis: lista de responses geradas pelo GPT
    :retur: Fala do gpt formata
    :rtype: string
    '''
    #Inicio as duas variaveis
    falaGPT_total = ""
    tokens = 0

    #Recebo as respostas do GPT e formato os valores
    for r in respostas:
        falaGPT = r.choices[0].message.content
        falaGPT = falaGPT.replace(".", ".\n")
        falaGPT_total = falaGPT_total + "||" + falaGPT
        tokens = tokens + r.usage.total_tokens

    manip.completaLog(variaveis[0], falaGPT_total, variaveis[1], tokens,variaveis[4],variaveis[5],modeloGPT)

    #Retorno a resposta do GPT formatada
    return falaGPT_total

#Escolhe qual sequencia de prompt vai ser usada para responder
def escolheParte(variaveis):
    '''
    Escolhe qual função chamar conforme o que está na variavel[0] -> seção
    '''
    secao = variaveis[0]

    if 100 <= secao < 200:
        if secao == 100:
            resposta = secao100(variaveis)
        elif secao == 110:
            resposta =  secao110(variaveis)
        elif secao == 120:
            resposta = secao120(variaveis)
        elif secao == 130:
            resposta = secao130(variaveis)
        elif  140 <=secao <= 141:
            resposta = secao140(variaveis)
        elif secao == 142:
            variaveis[2] = "Este chat está encerrado pois você informou que não gostaria de continuar."
            resposta = variaveis
        else:
            variaveis[2] = "Este chat está encerrado pois ocorreu um erro. Erro de seção tipo 01"
            resposta = variaveis

    elif 200 <= secao < 300:
        if secao == 205:
            resposta = secao205(variaveis)
        elif 210 <= secao < 218:
            resposta = secao210(variaveis)
        elif secao == 218:
            resposta = secao305(variaveis)
        elif 230 <= secao <= 240:
            resposta = secao230(variaveis)
        elif 240 <= secao <= 250:
            resposta = secao240(variaveis)
        elif 260 <= secao < 280:
            resposta = secao260(variaveis)
        elif 280 <= secao <= 288:
            resposta = secao280(variaveis)
        elif 290 <= secao < 300:
            variaveis[2] = "Este chat está encerrado pois você informou que não gostaria de continuar."
            resposta = variaveis
        else:
            variaveis[2] = "Este chat está encerrado pois ocorreu um erro. Erro de seção tipo 02"
            resposta = variaveis
    elif 300 <= secao < 400:
        if 300 <= secao < 310:
            resposta = secao300(variaveis)
        elif 310 <= secao < 320:
            resposta = secao310(variaveis)
        elif 320 <= secao < 330:
            resposta = secao320(variaveis)
        elif 330 <= secao < 340:
            resposta = secao330(variaveis)
        elif 340 <= secao < 350:
            resposta = secao340(variaveis)
        elif 350 <= secao < 360:
            resposta = secao350(variaveis)
        elif 370 <= secao < 380:
            variaveis[2] = "Este chat está encerrado."
            resposta = variaveis
            

      
        else: 
            variaveis[2] = "Este chat está encerrado pois ocorreu um erro. Erro de seção tipo 03"
            resposta = variaveis
    else:
        variaveis[2] = "Este chat está encerrado pois ocorreu um erro. Erro de seção tipo 04"
        resposta = variaveis
    return resposta

#-------------------------------------------------------------------------------------------------
#Verificadores da PARTE 1

#Verifica se o nome da pessoa foi dito
def verificaNome(variaveis):    
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system",
             "content": "Você está verificando se o usuário mencionou seu nome. Responda TRUE se o usuário mencionou seu nome ou como deseja ser chamado, e FALSE caso contrário."},
            {"role": "system",
             "content": "Exemplos: User:'Teodoro' asssistant: 'TRUE', User:'Não quero' asssistant:'FALSE', User:'Me chamo Pedro' asssistant:'TRUE', User:'Adoro poneis' assistant: 'FALSE'" +
             " User:'Bibi' assistant:'TRUE', User:'Me chame de Gustavo' asssistant:'TRUE', User:'Que legal você ser um robô' assistant: 'FALSE',  User:'Meu nome é  Claudio' asssistant:'TRUE', User:'Pode me chamar de Teodoro' asssistant:'TRUE', User:'Adoro nomes' assistant: 'FALSE'"},
            {"role": "user", "content": variaveis[1]},

        ]
    )

    if (response.choices[0].message.content.upper().__contains__("FALSE")):
        printVerificador("Falou nome", " A pessoa NÃO falou o nome!")
        if (variaveis[0] != 100):
            response = client.chat.completions.create(
                model=modeloGPT,
                messages=[
                    {"role": "assistant", "content": variaveis[2]},
                    {"role": "user", "content": variaveis[1]},
                    {"role": "system",
                    "content": "Responda explicando que não entedeu como a pessoa se chama e então diga que ela precisa explicar como chama-la.  Use no maximo 100 palavras"},
                ]
            )

            variaveis[2] = enviaResultados([response], variaveis)
            return False

    else:
        printVerificador("Falou nome", "A pessoa falou o nome!")
        return True

#Verifica se a pessoa pediu para repetir
def verificaRepete(variaveis):

    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "assistant", "content": variaveis[2]},
            {"role": "user", "content": variaveis[1]},
            # Responda, Sim, se a pessoa tiver
            {"role": "system",
             "content": "Responda TRUE se o usuario pediu para repetir, caso contrario, responda FALSE"},
        ]
    )

    if (response.choices[0].message.content.upper().__contains__("TRUE")):
        printVerificador("Repete Fala", "A pessoa pediu para repetir ou não entendeu o que foi dito!")
        response = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system", "content": variaveis[2]},
                {"role": "system", "content": "Explique que vai repetir o que tinha dito. "+
                 "Termine reformulando a frase acima sem perder o significado"},
            ]
        )
        falaGPT = enviaResultados([response], variaveis)
        variaveis[2] = falaGPT
        return True

    else:
        printVerificador("Repete Fala", "A pessoa não pediu para repetir e entendeu o que foi dito!")
        return False

#Verifica se a pessoa terminou o desafio
def verificaDesafio(variaveis):
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "assistant", "content": variaveis[2]},
            {"role": "user", "content": variaveis[1]},
            {"role": "system",
             "content": "Responda TRUE se a pessoa tiver aceito o desafio e FALSE se tiver negado "},
            {"role": "system",
             "content": "Exemplos: User:'Aceito o desafio' asssistant: 'TRUE', User:'Não quero' asssistant:'FALSE', User:'Topo participar' asssistant:'TRUE', User:'Não topo' assistant: 'FALSE'"},

        ]
    )

    falaGPT = response.choices[0].message.content
    printVerificador("Verifica Desafio", "verifica Desafio saida :" + str(falaGPT))

    if (response.choices[0].message.content.upper().__contains__("TRUE")):
        return True
    return False
    
#Verifica se a pessoa entendeu as regras
def verificaRegras(variaveis):
    
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            # Responda, Sim, se a pessoa tiver
            {"role": "assistant", "content": variaveis[2]},
            {"role": "user", "content": variaveis[1]},
            {"role": "system",
             "content": "Responda TRUE se a pessoa afirmar ou dizer que entendeu e FALSE ela negar ou dizer que não entendeu"},
        ]
    )

    if (response.choices[0].message.content.upper().__contains__("FALSE")):
        printVerificador("Verifica Regras", "A pessoa não entendeu as regras!")
        response = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system",
                 "content": "Diga que vai repetir e termine reformulando a frase abaixo mantendo o mesmo significado e para parecer que está falando com uma criança"},
                {"role": "user",
                 "content": "'As regras do desafio são as seguintes: Primeiro é preciso fazer perguntas para mim (Blabinha), essas perguntas tem que que ser sobre a o assunto " +
                            "Amazônia azul. Quanto mais você manter no assunto mais pontos vai ganhar. Caso não saiba sobre o que falar pode pedir dica de algum assunto." +
                            "Além disso você pode pedir para terminar e sair a hora que quiser'"},
            ]
        )
        variaveis[2] = enviaResultados([response], variaveis)
        return False
    else :
        printVerificador("Verifica Regras", "A pessoa disse que entendeu as regras!")
        return True

def casoTeste(variaveis):
    '''
    Caso criado para teste
    Vai para função de teste se escrito "jaguatirica"
    '''
    if(variaveis[1] == "jaguatirica"):
        variaveis[0] == 300
        return True
    return False
#-------------------------------------------------------------------------------------------------
#Verificadores da PARTE 2    

#Verifica se a pessoa pediu dica ou não
def verificaDica(variaveis):
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            # Responda, Sim, se a pessoa tiver
            {"role": "system", "content": "Responda TRUE se a pessoa pediu dica e FALSE se não pediu"},
            {"role": "user", "content": variaveis[1]},
        ]
    )

    if (response.choices[0].message.content.upper().__contains__("TRUE")):
        printVerificador("Verifica Dica", "A pessoa pediu alguma dica!")
        response = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system",
                 "content": "Amazônia Azul é a região que compreende a superfície do mar, águas sobrejacentes ao leito do mar, solo e subsolo marinhos contidos na extensão atlântica que se projeta a partir do litoral até o limite exterior da Plataforma Continental brasileira"},
                {"role": "system", "content": "Primeiro diga que vai dar dica de assuntos sobre a Amazônia Azul e termine enumerando 4 possiveis assuntos que estejam relacionados a Amazônia Azul."},
            ]
        )
        falaGPT  = enviaResultados([response], variaveis)
        variaveis[2] = falaGPT       
        return True


    else:
        printVerificador("Verifica Dica", "A pessoa não pediu nenhuma dica")
        return False

#Verifica se a pessoa pediu para terminar
def verificaTerminar(variaveis):
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            # Responda, Sim, se a pessoa tiver
            {"role": "system",
             "content": "Responda TRUE se a pessoa pediu para terminar ou acabar e FALSE se não pediu"},
            {"role": "user", "content": variaveis[1]},
        ]
    )

    if (response.choices[0].message.content.upper().__contains__("TRUE")):
        printVerificador("Verifica Termino", "A pessoa pediu para terminar!")
        response = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system",
                 "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no máximo 100 palavras"},
                {"role": "system", "content": "Pergunte se a pessoa realmente quer terminar. Diga que falta pouco para ela concluir e criar o herói"},
                {"role": "user", "content": variaveis[1]},
            ]
        )
        falaGPT  = enviaResultados([response], variaveis)
        variaveis[2] = falaGPT
        variaveis[0] = variaveis[0] + 50
        return True

    else:
        printVerificador("Verifica Termino", "A pessoa não pediu para terminar")
        return False

def verificaTerminar2(variaveis):
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            # Responda, Sim, se a pessoa tiver
            {"role": "assistant", "content": variaveis[2]},
            {"role": "user", "content": variaveis[1]},
            {"role": "system",
             "content": "Responda TRUE se a pessoa(user) pediu para terminar ou acabar e FALSE se não pediu"},
            
        ]
    )

    if (response.choices[0].message.content.upper().__contains__("TRUE")):
        printVerificador("Verifica Termino2", "A pessoa pediu para terminar!")
        response = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system",
                 "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no máximo 100 palavras"},
                {"role": "system", "content": "Pergunte se a pessoa realmente quer terminar. Diga que falta pouco para ela concluir e criar o herói"},
                {"role": "user", "content": variaveis[1]},
            ]
        )
        falaGPT  = enviaResultados([response], variaveis)
        variaveis[2] = falaGPT
        variaveis[0] = variaveis[0] + 10
        return True

    else:
        printVerificador("Verifica Termino", "A pessoa não pediu para terminar")
        return False

def verificaParte03(variaveis):
    frase = str.lower(variaveis[1])
    possibilidades = ["criar heroi","criar héroi","parte 3","parte 03"]

    if frase in possibilidades:
        response1 = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
            {"role": "system", "content": "Pergunte se a pessoa(criança) realmente quer ir para parte da criação de herói. Termine dizendo que quanto mais ela interagir mais forte o herói será."},
        ]
        )
        falaGPT  = enviaResultados([response1], variaveis)
        variaveis[2] = falaGPT
        variaveis[0] = variaveis[0] + 70
        return True

    else:
        printVerificador("Verifica Termino", "A pessoa não pediu para terminar")
        return False

#Verifica se a pessoa falou sobre o contexto da amazônia Azul
def verificaContexto(variaveis):
    contexto = (
        "Amazônia Azul é a região que compreende a superfície do mar, águas sobrejacentes ao leito do mar, solo e subsolo marinhos contidos na extensão atlântica que se projeta a partir do litoral até o limite exterior da Plataforma Continental brasileira."
        "Podemos resumir como tudo que envolve o Mar Brasileiro como animais, locais, navios,etc")
    

    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "assistant", "content": variaveis[2]},
            {"role": "user", "content": variaveis[1]},
            {"role": "system", "content": " Responda TRUE se o user tiver feito uma pergunta dentro do contexto da Amazônia Azul. Para decidir se uma pergunta está dentro do contexto da Amazônia azul existem 2 possibilidades:" 
            + "1 - É uma pergunta sobre o Brasil e sobre o mar, ou seja peixes, ilhas, barcos, o propio mar, etc. 2 - É uma pergunta diretamente sobre a Amazônia Azul, ou seja tem Amazônia Azul na pergunta. Responda FALSE se for sobre outro contexto"},
        ]
    )

    if (response.choices[0].message.content.upper().__contains__("FALSE")):
        printVerificador("Verifica Contexto", "NÃO está dentro do contexto")
        response = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "user", "content": variaveis[1]},
                {"role": "system",
                 "content": "Não responda o User, explique para ele que o assunto que ele falou não está relacionado com a Amazônia azul. Use no maximo 30 palavras"},
            ]
        )
        response1 = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system", "content": contexto},
                {"role": "system",
                 "content": "Explique que o user deve falar sobre Amazônia Azul e de 4 exemplos de assuntos que ele pode fala que sejam sobre a Amazônia Azul. Use no máximo 150 palavras"},
            ]
        )
        respostas = [response,response1]
        falaGPT = enviaResultados(respostas, variaveis)    
        falaRotativa = secao225(variaveis)
        variaveis[2] = falaGPT + falaRotativa  

        return False

    else:
        printVerificador("Verifica Contexto", "Falou sobre Amazônia Azul")
        return True

#Verifica se a pessoa falou alguma das palavras chaves
def verificaBonus(variaveis):
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "user", "content": variaveis[1]},
            {"role": "system",
            "content": "Você é uma analista de textos, e precisa ver se o texto fala de alguma forma sobre 'Governo'. Retorne como saida TRUE se for dito e FALSE se não for"},

        ]
    )

    falaGPT = response.choices[0].message.content

    if (falaGPT.upper()).__contains__("FALSE"):
        printVerificador("Verifica Bonus", "Caiu no caso Bonus")
        return False

    else:
        printVerificador("Verifica Bonus", "Não caiu no caso Bonus")
        return True
    
def repetiraCriação(variaveis):
    response = client.chat.completions.create(
    model=modeloGPT,
    messages=[
        {"role": "assistant", "content": variaveis[2]},
        {"role": "user", "content": variaveis[1]},
        {"role": "system",
            "content": "Responda TRUE se a pessoa quiser ir para criação e FALSE se não quiser"},
        ]
    )
    falaGPT = response.choices[0].message.content

    if (falaGPT.upper()).__contains__("FALSE"):
        printVerificador("Verifica Bonus", "Caiu no caso Bonus")
        return False

    else:
        printVerificador("Verifica Bonus", "Não caiu no caso Bonus")
        return True

def secao100(variaveis):
    if casoTeste(variaveis) is True:
        return secaoTeste(variaveis)

    if (verificaNome(variaveis) is True):
        print("caiu aqui")
        response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Seu objetivo é falar sobre a Amazônia Azul. Evite gerar perguntas. Use no máximo 100 palavras"},
            {"role": "user", "content": variaveis[1]},
            {"role": "system", "content": "Siga somente os passos para gerar o texto: Passo 1 - Reaja ao que a pessoa falou  Passo 2 - Exlique o que você é" +
                "Passo 3 - Por ultimo pergunte se pessoa já ouviu falar da Amazônia Azul."},
            ]
        )
        respostas = [response]    
        variaveis[2] = enviaResultados(respostas, variaveis)    
        variaveis[0] = 120
        return variaveis
    
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Seu objetivo é falar sobre a Amazônia Azul. Evite gerar perguntas. Use no máximo 100 palavras"},
            {"role": "user", "content": variaveis[1]},
            {"role": "system", "content": "Siga somente os passos para gerar o texto: Passo 1 - Reaja ao que a pessoa falou  Passo 2 - Exlique o que você é" +
                "Passo 3 - Por ultimo pergunte como pode chamar a pessoa."},

        ]
    )
    respostas = [response]    
    variaveis[2] = enviaResultados(respostas, variaveis)    
    variaveis[0] = 110
    return variaveis

def secao110(variaveis):

    if var.getLimite() < 2:
        if (verificaNome(variaveis) is False):
            var.addLimite()
            return variaveis
    else:
        response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "assistant", "content": variaveis[2]},
            {"role": "user", "content": variaveis[1]},
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." +
                                          "Evite gerar perguntas. Use no máximo 100 palavras."},
            {"role": "system", "content": "Diga que já que ela não quer falar o nome vamos seguir em frente e por ultimo pergunte se ela já ouviu fala na Amazônia Azul" },
            ]
        )
        respostas = [response]    
        variaveis[2] = enviaResultados(respostas, variaveis)    
        variaveis[0] = 120
        var.resetLimite()
        return variaveis
            
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "assistant", "content": variaveis[2]},
            {"role": "user", "content": variaveis[1]},
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." +
                                          "Evite gerar perguntas. Use no máximo 100 palavras."},
            {"role": "system", "content": "Para responder primeiro demonstre contentamento em conhecer a pessoa e por ultimo pergunte se ela já ouviu fala sobre a Amazônia Azul" },
        ]
    )
    respostas = [response]    
    variaveis[2] = enviaResultados(respostas, variaveis)    
    variaveis[0] = 120
    var.resetLimite()
    return variaveis

def secao120(variaveis):

    if verificaRepete(variaveis) is True:
            return variaveis

    
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system",
             "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no máximo 150 palavras."},
            {"role": "system", "content": "Siga somente os passos para gerar o texto:" +
                                          "Passo 1- Se a pessoa já souber sobre amazônia azul parabenize ela, se não diga algo reconfortante." +
                                          "Passo 2- Explique brevemente que o desafio consiste em criar um super-herói e para isso vai ser" +
                                          " preciso aprender sobre a amazônia azul" +
                                          "Passo 3 - CONVIDE ela para participar do desafio"},
            {"role": "assistant", "content": variaveis[2]},
            {"role": "user", "content": variaveis[1]},
        ]
    )
    respostas = [response]    
    variaveis[2] = enviaResultados(respostas, variaveis)    
    variaveis[0] = 130
    var.resetLimite()
    return variaveis

def secao130(variaveis):

    if verificaRepete(variaveis) is True:
        return variaveis

    if verificaDesafio(variaveis) is False:

        response = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system",
                 "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no máximo 100 palavras"},
                {"role": "assistant", "content": variaveis[2]},
                {"role": "user", "content": variaveis[1]},
                {"role": "system", "content": "Pergunte se realmente a pessoa não está querendo participar do desafio"},
            ]
        )

        respostas = [response]    
        variaveis[2] = enviaResultados(respostas, variaveis)    
        variaveis[0] = 140
        var.resetLimite()
        return variaveis
    
    else:
        response0 = client.chat.completions.create(
            model=modeloGPT,
            messages=[

                {"role": "system","content": "Você é um robô chamado Blabinha e está conversando com uma criança. Evite gerar perguntas. Explique o que é o desafio refazendo a frase abaixo e mantendo o mesmo significado"},
                {"role": "system", "content": "A criança fazer perguntas sobre a Amazônia Azul para você (Blabinha) de forma a criar um héroi. Quanto mais perguntas forem feitas mais forte o héroi será."},
            ]
        )
        response1 = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "assistant","content": response0.choices[0].message.content},
                {"role": "system","content": "Você é um robô chamado Blabinha e está conversando com uma criança. Evite gerar perguntas. Complemente a explicação do desafio refazendo a frase abaixo  e mantendo o mesmo significado"},
                {"role": "system", "content": "As regras do desafio são as seguintes: Primeiro explique que acontecem no máximo 7 turnos. Somente perguntas que a Blabinha entender como Amazônia Azul contam como turnos. Você (criança) pode pedir dicas sobre"+
                 "possiveis assuntos da Amazônia Azul. Além disso pode pedir para terminar, ou seja acabar o jogo. Ou pedir para criar o héroi em algum momento da interação.Termine dizendo que esses três ultimos casos não contam como turno"},
            ]
        )
        response2 = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "assistant","content": response1.choices[0].message.content},
                {"role": "system", "content": "Termine perguntando se a pessoa entendeu as regras. Use no maximo 40 palavras"}
            ]
        )


        respostas = [response1,response2]    
        variaveis[2] = enviaResultados(respostas, variaveis)    
        variaveis[0] = 205
        var.resetLimite()
        return variaveis

def secao140(variaveis):        
        
        result = verificaDesafio(variaveis)

        if(result is False and variaveis[0] < 141):
            response2 = client.chat.completions.create(
                model=modeloGPT,
                messages=[
                    {"role": "system",
                        "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no máximo 100 palavras"},
                    {"role": "assistant", "content": variaveis[2]},
                    {"role": "user", "content": variaveis[1]},
                    {"role": "system", "content": "Tente convencer a ela não terminar e participar do desafio"},
                ]
            )
            respostas = [response2]
            variaveis[2] = enviaResultados(respostas, variaveis)    
            variaveis[0] = variaveis[0] + 1
            return variaveis

        
        if(result is False and variaveis[0] == 141):
            response2 = client.chat.completions.create(
                model=modeloGPT,
                messages=[
                    {"role": "system",
                        "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no máximo 100 palavras"},
                    {"role": "assistant", "content": variaveis[2]},
                    {"role": "user", "content": variaveis[1]},
                    {"role": "system", "content": "Diga que tudo bem que ela não queira participar do desafio. Termine dizendo que esse chat vai ser encerrado e se quiser falar denovo tera de abrir um novo chat"},
                ]
            )
            respostas = [response2]
            variaveis[2] = enviaResultados(respostas, variaveis)    
            variaveis[0] = variaveis[0] + 1
            return variaveis

        
    
        response1 = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system",
                    "content": "Refaça a frase abaixo mantendo o mesmo significado e para parecer que está falando com uma criança"},
                {"role": "user",
                    "content": "As regras do desafio são as seguintes: Primeiro é preciso fazer perguntas para mim (Blabinha), essas perguntas tem que que ser sobre a o assunto " +
                            " Amazônia azul. Quanto mais você manter no assunto mais pontos vai ganhar. Caso não saiba sobre o que falar pode pedir dica de algum assunto." +
                            "Além disso você pode pedir para terminar e sair a hora que quiser"},
            ]
        )
        response2 = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system", "content": "Pergunte se a pessoa entendeu as regras. Use no maximo 40 palavras"}
            ]
        )

        respostas = [response1,response2]    
        variaveis[2] = enviaResultados(respostas, variaveis)    
        variaveis[0] = 205
        return variaveis

def secao205(variaveis):

    if verificaRegras(variaveis) is False:
        return variaveis

    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "user", "content": variaveis[1]},
            {"role": "system",
             "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no máximo 50 palavras."},
            {"role": "system",
             "content": "Explique que agora a pessoa precisa fazer perguntas sobre Amazônia Azul e que você vai responde-las"},
        ]
    )

    variaveis[2] = enviaResultados([response] , variaveis)
    variaveis[0] = 210    
    return variaveis

def secao210(variaveis):
    quests = [212,214,216]

    if verificaParte03(variaveis) is True:
        return variaveis 
    
    if verificaTerminar(variaveis) is True:
        return variaveis    
    
    if verificaDica(variaveis) is True:
        return variaveis
    
    if verificaContexto(variaveis) is False:
        return variaveis
    
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "user", "content": variaveis[1]},
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança use um tom infantil. Use no máximo 150 palavras."},
            {"role": "system", "content": "Amazônia Azul é a região que compreende a superfície do mar, águas sobrejacentes ao leito do mar, solo e subsolo marinhos contidos na extensão atlântica que se projeta a partir do litoral até o limite exterior da Plataforma Continental brasileira."
                                          "Podemos resumir como tudo que envolve o Mar Brasileiro, fauna, flora e microorganismos"},
            {"role": "system", "content": "Sabendo disso tudo responda a pergunta que foi feita"}

        ]
    )

    if variaveis[0] in quests:
        response1 = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "user", "content": variaveis[1] },
                {"role": "assistant", "content": response.choices[0].message.content},
                {"role": "system", "content": "Explique que vai fazer agora um questão sobre o assunto tratado. Use no máximo 50 palavras"},
            ]
        )
        response2 = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "user", "content": variaveis[1] },
                {"role": "assistant", "content": response.choices[0].message.content},
                {"role": "system", "content": "Dado o asssunto tratado gere uma questão contendo 4 alternativas e uma só resposta correta enumere elas de 1) a 4). Fale somente a questão e as alternativas, não passe a resposta."},
            ]
        )
        resposta = [response,response1,response2]
        variaveis[2] = enviaResultados(resposta, variaveis)
        variaveis[0] = variaveis[0] + 21
        return variaveis
    
    if not (verificaBonus(variaveis)):

        if(variaveis[3] < 1):
            response2 = client.chat.completions.create(
                model=modeloGPT,
                messages=[
                    {"role": "user", "content": variaveis[1]},
                    {"role": "assistant", "content": response.choices[0].message.content},
                    {"role": "system",
                        "content": "Demonstre animação e  diga que a pessoa caiu em um bonus! Pergunte a ela que ferramenta o super-heroi vai usar. Dado o assunto tratado dê 4 possibilidades"
                                "de ferramentas que o heroi pode usar para proteger o mar do Brasil. Enumere elas de 1) a 4) como se fosse uma pergunta com alternativas. Use no maximo 120 palavras "},
                ]
            )
            resposta = [response,response2]
            variaveis[0] = variaveis[0] + 31
            variaveis[2] = enviaResultados(resposta, variaveis)
            variaveis[3] = variaveis[3] + 1
            return variaveis
        
    resposta = [response]

    falaGPT = enviaResultados(resposta, variaveis)
    falaRotativa = secao225(variaveis)


    variaveis[0] = variaveis[0] + 1
    variaveis[2]  = falaGPT + falaRotativa

    return variaveis

def secao225(variaveis):
    print("\n--------  225  -------- ")
    alea = random.randint(1,4)
    if alea == 1:
        print("\n--------  caso1  -------- ")

        response = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system",
                 "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no maximo 30 palavras."},
                {"role": "system",
                 "content": "Diga que a pessoa pode fazer mais perguntas ou pode pedir para terminar"},
            ]
        )
    elif alea == 2:
        print("\n--------  caso2  -------- ")
        response = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system",
                 "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no maximo 30 palavras."},
                {"role": "system",
                 "content": "Diga que a pessoa pode fazer mais perguntas e também caso não saiba um assunto pode pedir dicas"},
            ]
        )
    elif alea == 3:
        print("\n--------  caso3  -------- ")
        response = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system",
                 "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no maximo 30 palavras."},
                {"role": "system",
                 "content": "Diga que a pessoa pode fazer mais perguntas mas não deve se esquecer que tem que falar sobre Amazônia Azul"},
            ]
        )
    else:
        print("\n--------  caso4  -------- ")
        response = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system",
                 "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no maximo 30 palavras."},
                {"role": "system",
                 "content": "Diga que a pessoa pode fazer mais perguntas"},
            ]
        )
        
    resposta = [response]

    falaGPT = enviaResultados(resposta, variaveis)

    return falaGPT

def secao230(variaveis):
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "assistant", "content": variaveis[2]},
            {"role": "user", "content": variaveis[1]},
            {"role": "system",
             "content": "Verifique se a resposta está certa. Parabenize se estiver correta e se estiver errada explique o que está errado e qual seria a correta. Use no máximo 50 palavras"},
        ]
    )
    resposta = [response]
    variaveis[0] = variaveis[0] - 20
    falaGPT = enviaResultados(resposta, variaveis)
    falaRotativa = secao225(variaveis)
    variaveis[2]  = falaGPT + falaRotativa
    return variaveis

def secao240(variaveis):
    printSecao(variaveis)
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "assistant", "content": variaveis[2]},
            {"role": "user", "content": variaveis[1]},
            {"role": "system",
             "content": "Usando no maximo 50 palavras de uma opnião sobre a escolha da pessoa."},
        ]
    )
    resposta = [response]
    falaGPT = enviaResultados(resposta, variaveis)
    variaveis[0] = variaveis[0] - 30
    falaRotativa = secao225(variaveis)
    variaveis[2]  = falaGPT + falaRotativa
    return variaveis

def secao260(variaveis):  
    def retornaValor(status):

        if status >= 260:
            estado = status - 260  
        if status >= 270:
            estado = status - 270  
        if status >= 280:
            estado = status - 280

        estado = estado + 210
        return estado
    
    result = verificaTerminar2(variaveis)

    if (result is True and variaveis[0] < 270):
        response2 = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system",
                    "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no máximo 150 palavras"},
                {"role": "assistant", "content": variaveis[2]},
                {"role": "user", "content": variaveis[1]},
                {"role": "system", "content": "Tente convencer a ela não terminar e continuar no desafio"},
            ]
        )
        respostas = [response2]
        variaveis[2] = enviaResultados(respostas, variaveis)    
        variaveis[0] = variaveis[0] + 10
        return variaveis
    
    elif ( result is True and variaveis[0] >= 270):
        response2 = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system",
                    "content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no máximo 150 palavras"},
                {"role": "assistant", "content": variaveis[2]},
                {"role": "user", "content": variaveis[1]},
                {"role": "system", "content": "Diga que tudo bem que ela não queira participar do desafio. Termine dizendo que esse chat vai ser encerrado e se quiser falar denovo tera de abrir um novo chat"},
            ]
        )
        respostas = [response2]
        variaveis[2] = enviaResultados(respostas, variaveis)    
        variaveis[0] = 295
        return variaveis
    else:        
        response1 = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system","content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no máximo 100 palavras"},
                {"role": "assistant", "content": variaveis[2]},
                {"role": "user", "content": variaveis[1]},
                {"role": "system",
                    "content": "Demonstre que está feliz pela pessoa não ter deistido e diga que ela pode continuar"},
            ]
        )


        respostas = [response1]    
        falaGPT = enviaResultados(respostas, variaveis)
        falaRotativa = secao225(variaveis)
        variaveis[2]  = falaGPT + falaRotativa          
        variaveis[0] = retornaValor(variaveis[0])
        return variaveis   

def secao280(variaveis):
    response = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "assistant", "content": variaveis[2] },
            {"role": "user", "content": variaveis[1] },
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
            {"role": "system", "content": "Verifique se a pessoa realmente quer seguir para criação do héroi. Responda TRUE se sim e FALSE se não."},
        ]
    )

    if (response.choices[0].message.content.upper().__contains__("TRUE")):
        return secao300(variaveis)
    
    print("caiu aqui")
    print("caiu aqui")
    print("caiu aqui")
    print("caiu aqui")

    response1 = client.chat.completions.create(
    model=modeloGPT,
    messages=[
        {"role": "system","content": "Você é um robô chamado Blabinha e está conversando com uma criança. Use no máximo 100 palavras"},
        {"role": "system",
            "content": "Demonstre que está feliz pela pessoa querer jogar mais e diga que ela pode continuar"},
    ]
    )


    respostas = [response1]    
    falaGPT = enviaResultados(respostas, variaveis)
    falaRotativa = secao225(variaveis)
    variaveis[2]  = falaGPT + falaRotativa          
    variaveis[0] = variaveis[0] - 70
    print(variaveis[0])
    return variaveis   

def secao300(variaveis):
    var.setPath(variaveis)

    response1 = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
            {"role": "system", "content": "Diga que agora para criar o héroi a pessoa(criança) precisa ter paciência pois você(blabinha) "+
             "precisa ler toda conversa com ajuda de um script e então avaliar. Diga também que a pessoa(criança) só pode escrever depois que a Blabinha falar algo. Termine dizendo que para começar basta a pessoa escrever qualquer coisa"},
        ]
    )
    falaGPT = enviaResultados([response1], variaveis)
    variaveis[2]  = falaGPT         
    variaveis[0] = 310
    return variaveis

def secao305(variaveis):
    var.setPath(variaveis)

    response1 = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
            {"role": "system", "content": "Diga que a pessoa conversou tanto que chegou no final e que agora vamos para criação do herói. Para criar o héroi a pessoa(criança) precisa ter paciência pois você(blabinha) "+
             "precisa ler toda conversa com ajuda de um script e então avaliar. Diga também que a pessoa(criança) só pode escrever depois que a Blabinha falar algo. Termine dizendo que para começar basta a pessoa escrever qualquer coisa"},
        ]
    )
    falaGPT = enviaResultados([response1], variaveis)
    variaveis[2]  = falaGPT         
    variaveis[0] = 310
    return variaveis

def secao310(variaveis):
    '''
    :Verifica o quanto a pessoa interagiu e da estrelas
    :Verifica a quantidade de topicos e da estrelas
    :Verifica se ela caiu em bônus
    :Verifica a quantidade de questões que foi achada
    :Escolher as caracteristicas
    '''

    file_path = var.getPath()

    topicos = parte3.geraTopicos(file_path)

    var.addStar(int(topicos[3]))

    estrelas = parte3.estrelasCompletude(file_path)

    var.addStar(int(estrelas))

    qQuestoes = parte3.analisaRespostas(file_path)

    bonus = manip.returnBonus(var.getPath())


    response1 = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
            {"role": "system", "content": "Explique que agora você vai começar a dar a pontuação do jogo." +
             "Depois, diga que analisando o quanto ela interagiu ela ganhou: " + str(estrelas) + "estrelas de um total de quatro"  +
             "Termine analisando a quantidade que a criança conseguiu"},
        ]
    )

    response2 = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
            {"role": "system", "content": "Siga os passos a seguir para gerar a saida:" +
             "1 - Explique que agora você vai fazer uma analise de topicos sobre toda conversa. 2 - Diga que ela falou" + topicos[0] + " e " + topicos[1] + " e " + topicos[2] +
             "Termine falando que ela conseguiu " + str(topicos[3]) + "estrelas por causa disso de um total de 4" },
        ]
    )


    if(bonus == False):
        response3 = client.chat.completions.create(
            model=modeloGPT,
            messages=[
                {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
                {"role": "system", "content": "Diga que a pessoa não conseguiu chamar nenhum bônus e por isso não ganhou nenhuma estrela!"},

            ]
        )
        var.addHeroFeature("nada")
    else:
        ferramenta = parte3.verificaBonus(bonus)
        response3 = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
            {"role": "system", "content": "Diga que a pessoa ganhou achou um bônus e por isso ganhou duas estrelas! Termine dizendo que a ferramenta :" + ferramenta + "vai ser usada pelo super-herói."},

            ]
        )
        var.addStar(2)
        var.addHeroFeature(ferramenta)

    if qQuestoes >= 1:
        response4 = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
            {"role": "system", "content": "Siga os passos a seguir para gerar a saida:" +
            "1 - Diga que a pessoa respondeu  "+ str(qQuestoes) +" perguntas de um total de 3 e que por isso ela vai poder escolher "+ str(qQuestoes + 1) + " atributos do herói." +
            "2 - Termine dizendo que o primeiro atributo é a roupa do super herói, então pergunte como ela quer que seja a roupa do herói" },
        ]
        )
        resposta = [response1,response2,response3,response4]
        variaveis[2] = enviaResultados(resposta,variaveis)
        variaveis[0] = parte3.escolheQuestões(qQuestoes)
    else:
        response4 = client.chat.completions.create(
        model=modeloGPT,
        messages=[
            {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
            {"role": "system", "content": "Siga os passos a seguir para gerar a saida:" +
            "1 - Diga que como a pessoa não respondeu corretamente nenhuma pergunta. E por isso só podera escolher uma caracteristica do herói" +
            "2 - Diga para ela não ficar triste pois mesmo não acertando podera escolher a cor da roupa do herói. "+ 
            "3 - Terminando perguntado qual cor de roupa ela quer para seu super herói?" },
        ]
        )
        resposta = [response1,response2,response3,response4]
        variaveis[2] = enviaResultados(resposta,variaveis)
        variaveis[0] = 352
    return variaveis

def secao320(variaveis):
    var.addHeroFeature(variaveis[1])
    response1 = client.chat.completions.create(
    model=modeloGPT,
    messages=[
        {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
        {"role": "system", "content": "Diga que o segundo atributo é a capa, então pergunte como ela quer que seja a capa do herói" },
    ]
    )
    resposta = [response1]
    variaveis[2] = enviaResultados(resposta,variaveis)
    if(variaveis[0] > 322):
        variaveis[0] = variaveis[0] + 10
    else:
        variaveis[0] = 350
    return variaveis

def secao330(variaveis):
    var.addHeroFeature(variaveis[1])
    response1 = client.chat.completions.create(
    model=modeloGPT,
    messages=[
        {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
        {"role": "system", "content": "Diga que o terceiro atributo é o companheiro de exploração, então pergunte qual companheiro o herói vai ter?" },


    ]
    )
    resposta = [response1]
    variaveis[2] = enviaResultados(resposta,variaveis)
    if(variaveis[0] > 333):
        variaveis[0] = variaveis[0] + 10
    else:
        variaveis[0] = 350
    return variaveis
    
def secao340(variaveis):
    var.addHeroFeature(variaveis[1])
    response1 = client.chat.completions.create(
    model=modeloGPT,
    messages=[
        {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
        {"role": "system", "content": "Diga que o quarto atributo é a casa do herói, então pergunte como será a casa do herói?" },


    ]
    )
    resposta = [response1]
    variaveis[2] = enviaResultados(resposta,variaveis)
    variaveis[0] = 350
    return variaveis

def secao350(variaveis):
    var.addHeroFeature(variaveis[1])

    response1 = client.chat.completions.create(
    model=modeloGPT,
    messages=[
        {"role": "system", "content": "Você é um robô chamado Blabinha e está conversando com uma criança." },
        {"role": "system", "content": " Diga que a pessoa conseguiu " + str(var.getStar())+" estrelas de um total de 10." +
            "Então reaja a quantidade de estrelas que ela ganhou. E termine dizendo que o héroi foi criado e que tem uma imagem dele."},

        ]
    ) 
    prompt = var.getHeroFeature()
    print(prompt)
    frase =  "Gere um heroi que vai proteger o oceano do Brasil. Ele tem as seguintes caracteristicas:" + prompt + "A sua força está ligada com a quantidade de pontos. Ele tem" + str(var.getStar()) + "pontos de um total de 10."
    imagem = client.images.generate(
        model="dall-e-3",
        prompt=frase,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    resposta = [response1]
    variaveis[2] = enviaResultados(resposta,variaveis)
    variaveis[2] = variaveis[2] + "\nlink para a imagem gerada:  " + imagem.data[0].url
    variaveis[0] = 371
    manip.saveImages(variaveis[4],variaveis[5],imagem.data[0].url)
    return variaveis

def secaoTeste(variaveis):
    var.pathTeste()
    return secao300(variaveis)
    