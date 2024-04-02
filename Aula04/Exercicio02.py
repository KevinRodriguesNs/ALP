salario = float(input('Digite seu salário atual:'))

aumento = float(input('Digite o aumento:'))

valor_aumento = salario*aumento/100

salario_novo = salario + valor_aumento

print('Seu novo salário é de:R$', salario_novo)


print(f'Salário atual: R${salario:8.2f}')
print(f'Aumento.......:R${valor_aumento:8.2f}')

print('------------------------------------------')

print(f'Novo Salário..:R${salario_novo:8.2f}')