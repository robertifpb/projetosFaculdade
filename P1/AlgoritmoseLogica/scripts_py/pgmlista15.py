num1 = []
num2 = []
for c in range(15):
    digite = int (input('Digite um número:'))
    num1.append(digite)
    num2.append(digite * 2)
print("Lista 1:", num1)
print("Lista 2:", num2)

def somarValores(valor1, valor2):
    soma= valor1 + valor2
    return soma

resultado = somarValores(num1[0], num2[0])
print("Soma do primeiro número da lista:", resultado)