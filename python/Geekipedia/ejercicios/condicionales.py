print("Sistema para calcular el promedio de un alumno")
nombre=input("¿Cuál es tu nombre?: ")

Matemáticas=int (input(nombre +" ¿Cuál es tu calificación en Matemáticas: "))
Química=int (input(nombre +" ¿Cuál es tu calificación en Química: "))
Biología=int (input(nombre +" ¿Cuál es tu calificación en Biología: "))

promedio=(Matemáticas+Química+Biología)/ 3
promedio = int(promedio)

if promedio >=6:
    print('Felicitaciones ' +nombre +' APROBASTE con un promedo de: ' , promedio)

print("Fin.")
