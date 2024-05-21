nome = input("Digite seu nome completo:")
nascimento = input("Digite a data de nascimento <DD/MM/AAAA>:")
data = nascimento.split('/')
palavra = nome.split()
pre_nome = palavra[0]
sobrenome = palavra[1]

print(f"Olá {pre_nome}... muito bonito seu sobrenome: {sobrenome}")
print(f"Você nasceu no dia no dia {data[0]} e no mês {data[1]}")