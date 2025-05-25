import requests


url = "https://deckofcardsapi.com/api/deck/ycs46g2k01su/"


def requisicao(endpoint,param={}):
   #print(param)
    if param!= {}:
        response = requests.get(url+endpoint,params=param)
    else:
        response = requests.get(url+endpoint)
    if response.status_code == 200:
        #print(response.json())
        return response.json()
    else:
        return []


def sacar(Jogador,quantidade=2):
    cartas = requisicao("draw","count="+str(quantidade))
    listcards =[]
    for carta in cartas['cards']:
        listcards.append(carta['code'])
    requisicao("pile/"+Jogador+"/add","cards="+(",").join(listcards))
    return pontos(Jogador)

def pegarCartas(Jogador):
    cartas = requisicao("pile/"+Jogador+"/list")["piles"][Jogador]["cards"]
    return cartas

def pontos(Jogador):
    cartas = requisicao("pile/"+Jogador+"/list")["piles"][Jogador]["cards"]
    return int(pontuacao(cartas))


def pontuacao(cartas):
    #print(cartas)
    pontos = 0
    for carta in cartas:
        code = carta['code'][0]
        if code not in ['J','Q',"K","A"]:
            if code == '0':
                pontos+=10
            else:
                pontos+=int(code)
        elif code == "A":
            if (len(cartas)==2 and pontos == 10):
                pontos+=11
            else:
                pontos+=1
        else:
            if pontos==1:
                pontos+=10
            pontos+=10
    return str(pontos)
        
        

requisicao("pile/jogador1/return")
requisicao("pile/jogador2/return")
requisicao("pile/mesa/return")
sacar("jogador1")
sacar("jogador2")
sacar("mesa")





