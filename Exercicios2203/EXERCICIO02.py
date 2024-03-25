p1 = float(input("Nota da prova 1:"))
p2 = float(input("Nota da prova 2:"))
media = ((p1+p2)/2)
if media>9:
    x= "A"
elif media>7.5:
    x= "B"
elif media>6:
    x= "C"
elif media>4:
    x= "D"
else:
    x= "E"


print("Prova 1:", p1)
print("Prova 2:", p2)
print("Média:", media)
print("Conceito:", x)
if (x=="A") or (x=="B") or (x=="C"):
    print("APROVADO")
else:
    print("REPROVADO")




