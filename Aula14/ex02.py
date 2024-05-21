def eprimo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

x = int(input("Digite um valor: "))
if eprimo(x):
    print("O valor digitado é primo!")
else:
    print("O valor digitado não é primo!")


def lista_primos(n):
    primos = []
    for num in range(0, n + 1):
        if eprimo(num):
            primos.append(num)
    return primos


numero = int(input("Digite um numero para calcular quantos numeros primo vem antes dele:"))
primos_lista1 = lista_primos(numero)
print(f"Segue a lista de numeros primos antes do valor {numero}: {primos_lista1}")

Y = 42
calc = Y * 2 + 5

primos_lista2 = lista_primos(calc)
soma_primos = sum(primos_lista2)

print(f"Lista de números primos considerando o final do meu RA = {Y}:  {primos_lista2}")
print(f"Somatoria de todos os numeros primos até o valor {calc} é: {soma_primos}")
