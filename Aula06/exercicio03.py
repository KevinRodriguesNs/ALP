#l_tinta = float(input("Quantos litros tem a lata de tinta?"))
a = float(input("Medida da parade A:"))
b = float(input("Medida da parade B:"))
porta = 0.80*2.10

area_a = (a*2.80)*2
area_b = (b*2.80)*2
area_total = area_a+area_a-porta

total_tinta = area_total/3

latas_tinta_18 = int(total_tinta / 18)
latas_tinta_37 = total_tinta / 3.7


print("Vai ser necessário ", latas_tinta_18, "latas de tinta de 18L")