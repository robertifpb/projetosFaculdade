import os #módulo da biblioteca importada, para o programa se comunicar com o sistema operacional.

print('*' *100)
print(f"{'calculadora de uso de tinta' .upper():^100}")
print('*' *100)

calcular_novamente = 's'
while calcular_novamente == 's':
    for calcular in range(2):
        nome = input(f'informe seu nome ({calcular+1}/2): ') .title()
        largura = float(input(f'{nome}, informe a largura em metros: '))
        altura = float(input(f'{nome}, agora informe a altura em metros: '))
        area = largura * altura
        tinta_necessaria = area / 2
        print('=' *100)
        print(f'{nome}, para pintar a área de {area:.2f}m², será necessário {tinta_necessaria:.1f} litros de tinta.')
        print('=' *100)
    calcular_novamente = input(f'{nome}, deseja calcular novamente? (s/n):') .lower()
    if calcular_novamente in ['s','n']:  
        os.system('cls' if os.name == 'nt' else 'clear') #os.system (detecta o sistema); 'cls' - windows, 'clear' - linux, mac

print('*' *100)
print(f"{f'{nome}, obrigado por utilizar o programa, até mais!' .upper():^100}")
print('*' *100)