frase = input("Digite uma frase:")
qnt = 0
for letra in frase:
    if (letra == "a") or (letra == "A") or (letra == "ã"): #pode ser assim tambem: if letra in 'AEIOUaeiou'
        qnt = qnt + 1
print (f"A letra 'a' aparece {qnt}.")