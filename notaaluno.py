alunos = {}

for i in range(3):
    nome = input("Digite o nome do aluno: ")
    nota = float(input("Digite a nota do aluno: "))
    alunos[nome] = nota

soma = 0
for nota in alunos.values():
    soma += nota

media = soma / len(alunos)

print("A média das notas dos alunos é:", media)