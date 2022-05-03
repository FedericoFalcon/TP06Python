''' 3. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en 
cada asignatura y guarde en una lista las aprobadas y en otra las desaprobadas. '''

asignaturas = ["Matematica","Fisica","Quimica","Historia","Lengua"]

listaAprobadas = []

listaDesaprobadas = []

nro = 0

for i in range(len(asignaturas)):
    print(asignaturas[nro])
    nota = int(input("Nota? "))
    if nota >= 6:
        listaAprobadas.append(asignaturas[nro])
    else:
        listaDesaprobadas.append(asignaturas[nro])
    nro = nro + 1

print("Lista aprobadas: ",listaAprobadas)
print("Lista desaprobadas: ",listaDesaprobadas)




