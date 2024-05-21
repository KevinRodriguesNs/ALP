n = input("Digite um número que seja positivo:")
soma = 0
mult = 1

for numero in n:
    numero_x = int(numero)
    soma = soma + numero_x
    mult = mult * numero_x

print(f"O total das soma dos digitos é {soma}, e o total da multiplicação é {mult}.")
