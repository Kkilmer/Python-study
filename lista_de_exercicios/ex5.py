#Crie um vetor N que seja resultado da soma 
#dos itens de outros dois vetores A e B. 
#Exemplo: A[0] + B[0] deverá ser salva em N[0].

A = [
    1, 2, 3,
    4, 5, 6
]

B = [
    7, 8, 9,
    10,11,12
]

soma = A + B
N = []
for i in range(len(soma)):
    for j in range(len(soma[i])):
        N.append(soma[i][j])
        print(N)