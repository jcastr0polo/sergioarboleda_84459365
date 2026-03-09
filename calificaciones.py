"""Programa de calificaciones (sin funciones).

Pide nombre, edad y calificación de 5 estudiantes usando solo
variables, bucles y condicionales. Valida edad (5-100) y
calificación (0-5). Muestra el mayor, el menor y el promedio.
"""

NUM_ESTUDIANTES = 5
estudiantes = []

for i in range(1, NUM_ESTUDIANTES + 1):
	print("\nEstudiante {}:".format(i))

	# Nombre (no vacío)
	while True:
		nombre = input("  Nombre: ").strip()
		if nombre != "":
			break
		print("  El nombre no puede estar vacío.")

	# Edad (entero entre 5 y 100)
	while True:
		edad_raw = input("  Edad: ")
		try:
			edad = int(edad_raw)
		except Exception:
			print("  Entrada inválida. Introduce un número entero.")
			continue
		if edad < 5 or edad > 100:
			print("  Edad fuera de rango. Debe estar entre 5 y 100.")
			continue
		break

	# Calificación (float entre 0 y 5)
	while True:
		nota_raw = input("  Calificación (0-5): ")
		try:
			nota = float(nota_raw)
		except Exception:
			print("  Entrada inválida. Introduce un número (ej. 4.5).")
			continue
		if nota < 0.0 or nota > 5.0:
			print("  Calificación fuera de rango. Debe estar entre 0 y 5.")
			continue
		break

	estudiantes.append({"nombre": nombre, "edad": edad, "nota": nota})

# Determinar mayor, menor y promedio usando bucles y acumuladores
if len(estudiantes) == 0:
	print("No hay estudiantes.")
else:
	mayor = estudiantes[0]
	menor = estudiantes[0]
	suma = 0.0
	idx = 0
	while idx < len(estudiantes):
		est = estudiantes[idx]
		suma = suma + est["nota"]
		if est["nota"] > mayor["nota"]:
			mayor = est
		if est["nota"] < menor["nota"]:
			menor = est
		idx = idx + 1

	promedio = suma / len(estudiantes)

	print("\nResultados:")
	print("  Mayor calificación: {} -> {:.2f}".format(mayor["nombre"], mayor["nota"]))
	print("  Menor calificación: {} -> {:.2f}".format(menor["nombre"], menor["nota"]))
	print("  Calificación promedio: {:.2f}".format(promedio))

