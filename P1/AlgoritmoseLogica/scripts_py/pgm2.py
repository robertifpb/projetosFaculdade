numeros = []
<<<<<<< HEAD
pares = []
impares = []

for i in range(20):
    num = int(input(f'Digite o {i+1}° número:'))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print("\nLista completa:", numeros)
print("Números pares:", pares)  
print("Números impares:", impares)     
=======
for i in range(15):
    num = int (input(f"Digite o {i+1}° número: "))
    numeros.append(num)

print("\n Lista de números digitados: ", numeros)   

maior = max(numeros)
menor = min(numeros)
pos_maior =  numeros.index(maior) + 1
pos_menor =  numeros.index(menor) + 1

print("\f Maior Valor: {maior}, na posição (maior)")
print("\f Menor Valor:{menor}, na posição (menor)")
>>>>>>> 29a7e3a8ff2d9666f95dc24e12b2eb8656811103
