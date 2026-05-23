
matriz = [[0 for j in range(4)] for i in range(5)]

maior_nota = 0
matricula_maior = 0


for i in range(5):

    matriz[i][0] = int(input("Matricula: "))
    matriz[i][1] = int(input("Media das provas: "))
    matriz[i][2] = int(input("Media dos trabalhos: "))

    
    matriz[i][3] = matriz[i][1] + matriz[i][2]

  
    if matriz[i][3] > maior_nota:
        maior_nota = matriz[i][3]
        matricula_maior = matriz[i][0]


print("\nMatriz completa:\n")

for i in range(5):
    for j in range(4):
        print(matriz[i][j], end=" ")
    print()
    
print("\nMatricula do aluno com maior nota final:")
print(matricula_maior)