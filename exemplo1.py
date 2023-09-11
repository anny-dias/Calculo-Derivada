def funcao(x_0):
    f = x_0**4 - x_0**3 - 3*x_0**2 + 1
    return f

def derivada(x_0):
    df = 4*x_0**3 - 2*x_0**2 - 6*x_0 
    return df

chute_inicial = 5

for i in range(10):
    y_o = funcao(chute_inicial)
    k = derivada(chute_inicial)
    chute_inicial = chute_inicial - y_o/k
    print(chute_inicial)