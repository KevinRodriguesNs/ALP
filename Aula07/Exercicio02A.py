n = int(input("Digite o valor:"))
E = 0
k = 1
while k <= n:
    E = E + 2**k
    k = k + 1
print(f"O valor de E = {E}")

