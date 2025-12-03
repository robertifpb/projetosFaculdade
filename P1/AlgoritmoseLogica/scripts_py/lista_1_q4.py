import os

print('\n' + '=' *100)
print(f"{'operações relacionais'.upper():^70}")
print('\n' + '=' *100)
mostrar_novamente = 's'
while mostrar_novamente == 's':
    for i in range(2):
        nome = input(f'Informe seu nome ({i+1}/2): ') .title()
        valor_a = int(input(f'{nome}, informe um valor: '))
        valor_b = int(input(f'{nome}, informe outro valor: '))
        condicao_1 = valor_a == valor_b
        condicao_2 = valor_a != valor_b
        condicao_3 = valor_a > valor_b
        condicao_4 = valor_a < valor_b
        condicao_5 = valor_a >= valor_b
        condicao_6 = valor_a <= valor_b
        print('\n' + '=' *100)
        print(f'{nome}, esses são os possíveis resultados das comparações: \n'
            f'\tO valor A ({valor_a}) é igual ao valor B ({valor_b})? {condicao_1}\n'
            f'\tO valor A ({valor_a}) é diferente do valor B ({valor_b})? {condicao_2}\n'
            f'\tO valor A ({valor_a}) é maior que o valor B ({valor_b})? {condicao_3}\n'
            f'\tO valor A ({valor_a}) é menor que o valor B ({valor_b})? {condicao_4}\n'
            f'\tO valor A ({valor_a}) é maior ou igual ao valor B ({valor_b})? {condicao_5}\n'
            f'\tO valor A ({valor_a}) é menor ou igual ao valor B ({valor_b})? {condicao_6}.')
    mostrar_novamente = input(f'{nome}, deseja fazer novamente? (s/n)')
    if mostrar_novamente in ['s', 'n']:
        os.system('cls' if os.name == 'nt' else 'clear')
print('\n'+ '=' *100)
print(f"{'fim!!!' .upper():^70}")
print('\n' + '=' *100)
