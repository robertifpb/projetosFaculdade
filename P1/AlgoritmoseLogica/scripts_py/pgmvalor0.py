numero = int(input("Digite um número:"))
contador = 0
while (numero!=0):
    if (numero >=100 and numero <= 200):
         contador = contador + 1
    numero=int(input("Digite um número:"))

print(contador)