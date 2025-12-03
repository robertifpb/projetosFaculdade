import os 
print('-' * 100)
print(f"{'conversor de hexadecimal para decimal' .upper():^100}")
print('-' * 100)

usar_nomamente = 's'
while usar_nomamente == 's':
    for i in range(1):
        
        def hexadecimal_para_decimal(hexadecimal_str):
            return int(hexadecimal_str, 16)

        numero_hexadecimal = input(f'Digite um número hexadecimal (sem 0x) ({i+1}): ').strip()
        numero_decimal = hexadecimal_para_decimal(numero_hexadecimal)
        print(f"O número {numero_hexadecimal.upper()} em decimal é {numero_decimal}.")

    usar_nomamente = input('Deseja usar novamente (s/n): ') .lower()

    if usar_nomamente in ['s','n']:
        os.system('cls' if os.name == 'nt' else 'clear')
print('-' * 100)
print(f"{'Obrigado por usar, até breve!' .upper():^100}")
print('-' * 100)