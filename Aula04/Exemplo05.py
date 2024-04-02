from math import pow, sqrt


x1 = float(input('Valor de x1:'))
x2 = float(input('Valor de x2:'))
y1 = float(input('Valor de y1:'))
y2 = float(input('Valor de y2:'))

dx = x2-x1
dy = y2-y1

d = sqrt(pow(dx,2)+pow(dy,2))

print('Distancia:',d)