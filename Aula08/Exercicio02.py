nascimento = input("Digite a data de nascimento DD/MM/AAAA:")
data = nascimento.split('/')
dia = data[0]
mes = data[1]
ano = data[2]
data_banco = ano+mes+dia
print(nascimento, "-", data_banco)