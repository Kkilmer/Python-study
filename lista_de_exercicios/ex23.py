#Dado uma lista de dicionários, onde cada dicionário representa um filme com as chaves 
#"título", "ano" e "gênero", crie um algoritmo que retorne a lista de 
#filmes ordenada primeiro por gênero e depois por ano.

filmes = {
    1: ['Outono em NY','Romance', 120, 1999],
    2: ['Exorcista', 'Terror', 324, 2023],
    3: ['Jhon Whik', 'Acao', 511, 2020]
}

for indice in filmes: #pesquisar como trazer dois valores?
    print(f'Filme: {filmes[indice][0]}')
    print(f'Gênero: {filmes[indice][1]}')
    print(f'Ano: {filmes[indice][3]}')
    print('-------')