#Biblioteca
import as np

#Main
notas = []
nomes = []
for i in range(5):
  n = input("Por favor insira o nome do aluno %d: " % (i+1))
  nomes.append(n)
  j = float(input("Por favor insira a nota do aluno %d: " % (i+1)))
  notas.append(j)

#aluno com maior nota
nosso_max = max(notas)
for i in range(5):
  if(notas[i] == nosso_max): 
    print("O aluno com maior nota é o %s" % nomes[i])

#média da turma
print("A média da turma é %.2f" % np.average(notas))
