# Autor: Pietro Henrique de Souza
# TP2 - Algoritmo de Dijkstra - Menor Caminho - PO - 2019 - PROF - Luciana Assis


# define os Nós seguidos com o pesos das arestas
grafo = {'A':{'B':1,'C':1,'D':5},   

         'B':{'A':1,'D':1},

         'C':{'A':1,'D':5,'E':5},

         'D':{'B':1,'C':5,'E':1},

         'E':{'C':5,'D':1}}


def dijkstraCaminhoMinimo(grafo,origem,destino):
    caminho_anterior = {}
    nao_visitados = grafo
    infinito = float("inf") #nos definidos como infinito enquanto não foram visitados
    menor_caminho = {}
    peso = []
    for no in nao_visitados:
        menor_caminho[no] = infinito #declara o menor caminho como infinito antes de ser encontrado
        
    menor_caminho[origem]=0 #menor caminho inicial declarado como 0   
        
    while nao_visitados:
        minNo = None
        for no in nao_visitados: #percorre por todos para ver se tem algum que não foi visitado
            if minNo is None:
                minNo = no
            elif menor_caminho[no] < menor_caminho[minNo]: #se o menor caminho minimo for menor q o no atual, ele irá atualizar
                minNo = no


        for childNode, weight in grafo[minNo].items():
            if weight + menor_caminho[minNo] < menor_caminho[childNode]:
                menor_caminho[childNode] = weight + menor_caminho[minNo] #peso + menor caminho
                caminho_anterior[childNode] = minNo
        nao_visitados.pop(minNo) #remove um elemento na lista (último) e e retorna o valor desse elemento


    no_atual = destino #no atual será o fim
    
    while no_atual != origem: #no atual será diferente do inicio
        try:
            peso.insert(0,no_atual)
            no_atual = caminho_anterior[no_atual]
            #criando uma exceção caso tenho erro no caminho
        except KeyError:
            print('Erro no caminho')
            break #se tiver erro, o programa para aqui
    peso.insert(0,origem)
    #menor caminho encontrado, sendo difente de infinito
    if menor_caminho[destino] != infinito:

    

        print ('\n           ALGORITMO CAMINHO MÍNIMO DIJKSTRA\n')
        print('        A distância do menor caminho é -> ' +str(menor_caminho[destino])) #encontra a menor distancia da origem ao destino, e imprime na tela
        
        print('\n                  CAMINHO PERCORRIDO\n')
        print('        O menor caminho percorrido será -> '+ str(peso)) #mostra o caminho a ser percorrido entre os nos e arestas


dijkstraCaminhoMinimo(grafo,'A','E') #origem ao destino