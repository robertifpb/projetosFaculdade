print('\n' + '=' *100)
print('\tinvertendo valores'.upper() .center(60))
print('\n' + '=' *100)
a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
a,b = b,a
print('\n' + '=' *100)
print(f'\tO valor da variável A agora é {a}.\n'
    f'\tO valor da variável B agora é {b}.')
print('\n' + '=' *100)
print('\tfim' .upper() .center(60))