print('\n' + '*' *100 )
print(f"{'bônus de natal'.upper():^80}")
print('\n' + '*' *100)

nomes = []
salarios = []
bonuses = []
totais = []

calcular_novamente = 's'
while calcular_novamente == 's':
    for i in range(2):
        nome_empregado =  input(f'Informe seu nome ({i+1}/2):') .title()
        salario = float(input(f'{nome_empregado}, informe seu salário: '))
        bonus =  salario * 0.6
        total = salario + bonus
        nomes.append(nome_empregado)
        salarios.append(salario)
        bonuses.append(bonus)
        totais.append(total)
        print('\n' + '*' *100)
        print(f'{nome_empregado}, seu salário de R$:{salario} reais, com o aumento de 60% da empresa,\n' 
        f'você receberá R$:{total:.2f} reais, com bonificação.')
        print('\n'+ '*' *100)
    calcular_novamente = input(f'{nome_empregado}, deseja calcular novamente? (s/n)')
print('\n' + '*' *100)
print(f"{'relatório de bônus de natal' .upper():^80}")
print('\n' + '*' *100)

for i in range(len(nomes)):
    print(f"{nomes[i]}: Salário: {salarios[i]:.2f}, Bônus: {bonuses[i]:.2f}, Total: {totais[i]:.2f}.")

print('\n' + '*' *100)
print(f"{'boas festas' .upper():^80}")
print('\n' + '*' *100)