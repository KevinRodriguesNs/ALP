l = {}
for _ in range (3):
    nome = (input(f"Digite seu nome:"))
    idade = int(input(f"Digite sua idade:"))
    dic = dict(nome=idade)
    l [nome] = idade

mais_velho = max(l, key=l.get)

print(f"O Nome da pessoa mais velha é {mais_velho}")