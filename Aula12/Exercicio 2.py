def eprimo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def lista_primos_ate(n):
    primos = []
    for num in range(2, n + 1):
        if eprimo(num):
            primos.append(num)
    return primos

# Verificação se um número é primo
x = int(input("Digite um valor: "))
if eprimo(x):
    print("O valor digitado é primo!")
else:
    print("O valor digitado não é primo!")

# Calcula os números primos até um dado número
numero = int(input("Digite um numero para listar todos os números primos até ele: "))
primos_lista1 = lista_primos_ate(numero)
print(f"Segue a lista de numeros primos até o valor {numero}: {primos_lista1}")


Y = 42
calc = Y * 2 + 5

primos_lista2 = lista_primos_ate(calc)
soma_primos = sum(primos_lista2)

print(f"Lista de números primos até {calc}, considerando meu RA = {Y}: {primos_lista2}")
print(f"Somatória de todos os números primos até o valor {calc}: {soma_primos}")
