#Escreva um algoritmo que permita a leitura das 
#notas de uma turma de 20 alunos. 
#Calcular a média da turma e contar quantos alunos 
#obtiveram nota acima desta média calculada.
#Escrever a média da turma e o resultado da contagem.

def media_turma():

  soma = 0

  for i in range(1, 21):
    
    nota = float(input("Insira a nota do {}º Aluno: ".format(i)))
    soma += nota
  media = soma / 20

  print("\nMédia da Turma: {:.2f}".format(media))
  count = sum([1 for nota in range(soma) if nota > media])
  print("Alunos com Nota Acima da Média: ", count)
  return media, count

media, count = media_turma()
