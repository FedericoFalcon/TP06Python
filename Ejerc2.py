#  2. Generar una lista X de 100 números reales entre -5 y 5, seguidamente generar la lista Y con la 
#  función f(x) = 2X^2 - 10. 
#  Ayuda: usar randint() para generar números aleatorios

from random import randint

lista = []
listaFuncion = []

for X in range(100):
    lista.append(randint(-5,5))

for X in lista:
    listaFuncion.append(2 * X ** 2 - 10)

print(lista)
print()
print(listaFuncion)

