#Desenvolva um programa para ler um vetor Q de 20 posições 
#(aceitar somente números positivos). Escrever a seguir:

#o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor;
#o valor do menor elemento de Q e a respectiva posição que ele ocupa no vetor;

from random import randint

Q = []

for numero in range(20):
    Q.append(randint(1, 100))

print(Q)
