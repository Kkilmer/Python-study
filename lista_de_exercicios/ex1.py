#Escreva um algoritmo que permita a leitura dos nomes de 10 clubes de futebol 
#e armazene os nomes lidos em um vetor (lista). Após isto, o algoritmo deve 
#permitir a leitura de mais 1 nome qualquer de clube e depois escrever a 
#mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente 
#(guardados no vetor), ou NÃO ACHEI caso contrário.

#Criar um lista com 5 clubes

clubes_de_futebol = [
    'ibis',
    'flamengo',
    'perilima',
    'volta redonda',
    'nacional de patos'
]

# Perguntar qual clube o usuário vai verificar
clube_pesquisado = input('Digite o clube: ')

for clube in clubes_de_futebol:

    if clube == clube_pesquisado:
        print('Achei')
    else:
        print('Ainda não achei!')