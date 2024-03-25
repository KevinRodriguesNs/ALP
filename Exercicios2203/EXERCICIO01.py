hora = float(input("Quantidade de hora feita no mês:"))
valor = float(input("Valor da hora:"))
salario = hora*valor
sindicato = ((salario/100)*3)
fgts = ((salario/100)*11)
inss = ((salario/100)*10)
#Calculo imposto de renda
if salario <= 900:
    ir = 0
    aliquota = 0
elif salario <=1500:
    ir = ((salario/100)*5)
    aliquota = 5
elif salario <= 2500:
    ir = ((salario/100)*10)
    aliquota = 10
else:
    ir = ((salario/100)*20)
    aliquota = 20

desconto = ir+inss+sindicato
salario_liquido = salario-desconto


print("Salário Bruto R$",salario)
print("IR:R$", ir)
print("INSS:R$", inss)
print("FGTS:R$", fgts)
print("Sindicato:R$", sindicato)
print("Total de desconto:R$", desconto)
print("Salário Liquido:R$", salario_liquido)