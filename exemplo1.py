import random

def funcao(x_0):
    f = x_0**4 - x_0**3 - 3*x_0**2 + 1
    return f

def derivada(x_0):
    df = 4*x_0**3 - 3*x_0**2 - 6*x_0 
    return df

lista_chute_inicial = [random.randint(-10,10) for i in range(10)]
lista_resultados = []
for i in range(len(lista_chute_inicial)):
    chute_inicial = lista_chute_inicial[i]
    for i in range(10):
        y_o = funcao(chute_inicial)
        k = derivada(chute_inicial)
        chute_inicial = chute_inicial - y_o/k
        print(chute_inicial)
    lista_resultados.append(chute_inicial)
