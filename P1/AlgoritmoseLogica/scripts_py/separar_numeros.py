numeros = []
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