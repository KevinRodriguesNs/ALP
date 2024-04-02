niver = float(input('Digite o ano que você nasceu:'))
ano = float(input('Digite o ano atual:'))

idade = ano-niver
meses = idade*12
semanas = idade*52
dias = idade*365

print('Você tem', idade, 'anos.')
print('Você tem', meses, 'meses de vida.')
print('Você tem', semanas, 'semanas de vida.')
print('Você tem', dias, 'dias de vida')