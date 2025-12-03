""""
print ('*' * 100)
print (f"{'interpolação de strigs'.upper():^100}")
print ('*' * 100)

nome = 'Robert'
valor = 70.00000055
variavel = '%s, valor será R$: %.2f' %(nome,valor)

print(variavel)
"""

def radar_de_multas():
    print('-' * 100)
    print(f"{'radar de multas'.upper():^100}")
    print('-' * 100)

    condutor =  input(f'Informe o nome do condutor: ') .title()
    velocidade = float(input(f'{condutor}, informe a velocidade atual do veículo: '))
    km_estrada = float(input(f'{condutor}, informe o KM onde o carro está na estrada: '))

    nova_solicitacao = 'CONTINUAR'
    while nova_solicitacao == 'CONTINUAR':
                
        RADAR_1 = 70
        LOCAL_1 = 100
        RADAR_RANGER = 1

        velocidade_permitida_radar = velocidade > RADAR_1
        veiculo_passou_radar = km_estrada >= (LOCAL_1 - RADAR_RANGER) and km_estrada <= (LOCAL_1 + RADAR_RANGER)
        multar_veiculo = veiculo_passou_radar > (RADAR_1 or LOCAL_1) and velocidade_permitida_radar > (RADAR_1 or LOCAL_1)

        if velocidade_permitida_radar:
            print(f'{condutor}, velocidade do veículo passou do radar 1, cuidado!')

        elif veiculo_passou_radar:
            print(f'{condutor}, veículo passou do radar 1.')

        elif multar_veiculo:
            print(f'{condutor}, você foi multado!')

        else:
            print(f'{condutor}, parabéns! Você se comportou bem no trânsito.')
            break
    nova_solicitacao = input(f"{condutor}, deseja encerrar o programa? (SAIR, CONTINUAR):")

    match nova_solicitacao:
        case 'SAIR':
            print('Programa encerrado')
        case 'CONTINUAR':
            print('Continue usando')

    print('-' * 100)
    print(f"{'assunto relacionado a complexidade de código, variáveis e constantes'.title():^100}")
    print('-' * 100)

radar_de_multas()