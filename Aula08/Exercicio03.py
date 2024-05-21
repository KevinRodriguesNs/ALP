frase = input("Digite a frase:").upper()
v = 0
for letra in frase:
    if letra in "AEIOU":
        v = v + 1

print(f"A frase tem {v} vogal(is).")