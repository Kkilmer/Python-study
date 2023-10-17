#Desenvolva um programa para ler um vetor Q de 20 posições 
#(aceitar somente números positivos). Escrever a seguir:

#o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
#o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

from random import randint

Q = []

for numero in range(20):
    Q.append(randint(1, 100))

#Variável de controle
maior = -1
menor = 101

for i in Q:
    if maior < i:
        maior = i

    if menor > i:
        menor = i

    print('Lista de números:')
    print(Q)
    print(f'O maior valor é: {maior}')
    print(f'O menor valor é: {menor}')

    print(max(Q))
    print(min(Q))



