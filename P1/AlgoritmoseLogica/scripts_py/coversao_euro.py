import os
def conversor_de_euro():

    print('*' * 100)
    print(f"{'conversor de euro para real' .upper():^100}")
    print('*' * 100)

    reutilizar_o_programa = 's'
    while reutilizar_o_programa == 's':
        for i in range(1):
            valor_em_euro = float(input(f'Informe o valor em euros ({i+1}): '))
            valor_cotacao = float(input('Informe o valor de cotação do Euro: '))
            valor_conversao = valor_em_euro * valor_cotacao
            valor_em_reais = valor_conversao
    print('-' * 100)
    print(f'O valor de {valor_em_euro} euros, corresponde a R$: {valor_em_reais:.2f} reais.')
    reutilizar_o_programa = input(f"{'deseja utilizar novamente? (s/n):'}")

    if reutilizar_o_programa in ['s','n']:
        os.system('cls' if os.name == 'nt' else 'clear')
    print('*' * 100)
    print(f"{'fim' .upper():^100}")
    print('*' * 100)    

conversor_de_euro()