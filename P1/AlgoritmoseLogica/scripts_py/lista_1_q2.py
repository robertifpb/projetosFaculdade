print('\n' + '-' *100)
print('conversor de real (R$) em dólar (US$)'.center(80).upper())
print('\n' + '-' *100)

repetir = 's'
while repetir == 's':
    for i in range(2):
        nome = input(f'Por favor, informe seu nome ({i+1}/2): ') .title()
        valor_cotacao = float(input(f'{nome}, informe o valor da cotação do dólar US$: '))
        quantidade_converter = float(input(f'{nome}, agora informe quantidade de dólares US$: '))
        print('\n' + '-' *100)
        conversão = valor_cotacao * quantidade_converter
        print(f'{nome}, o valor de US$: {quantidade_converter:,.2f} dólares, corresponde à R$: {conversão:,.2f} reais.')
    repetir = input (f'{nome}, deseja converter mais algum número? (s/n)')
print('\n' + '-' *100)
print('fim' .center(80).upper())
print('\n' + '-' *100)

#utilização da f-string , = separar a partir de milhões