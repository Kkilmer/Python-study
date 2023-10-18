#Dado uma lista de números, crie um algoritmo que retorne a soma dos números pares na lista.

#Exemplo de entrada: [1, 2, 3, 4, 5, 6]
#Saída esperada: 12

from random import randint

lista = []
resultado_da_soma = 0

for n in range(10):
    lista.append(randint(1, 30))

for i in lista:
    if(i % 2) == 0:
        resultado_da_soma = resultado_da_soma + i

print(f'O resultado da soma é: {resultado_da_soma}')

