valor_compra = float(input("Valor da compra: R$"))

if valor_compra<=1000:
    desconto = 10
elif valor_compra<=5000:
    desconto = 20
else:
    desconto = 30

desconto_compra = ((valor_compra/100)*desconto)

print("O desconto foi de:", desconto,"%")
print("Total de desconto: R$", desconto_compra)