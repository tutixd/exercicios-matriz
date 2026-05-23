matriz = [
   [1, 2, 3, 4],
   [5, 6, 7, 8],
   [9,10,11,12],
   [13,14,15,16]
]
maior = matriz[0][0]
for linha in matriz:
    for numero in linha:
        if numero > maior:
            maior = numero

print(maior)
