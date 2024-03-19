a = float(input("Lado A:"))
b = float(input("lado B:"))
c = float(input("lado C:"))
if (((a+b)<c) or ((a+c)<b) or ((b+c)<a)):
    print ("não é um triângulo")
elif (a==b==c):
    print ("é um triângulo Equilátero")
elif (a==b) or (b==c) or (a==c):
    print ("é um triângulo Isósceles")
else:
    print ("é um triângulo Escaleno")