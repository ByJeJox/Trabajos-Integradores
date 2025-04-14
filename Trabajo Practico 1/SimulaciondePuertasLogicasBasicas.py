def simulacion_puertas_logicas():
    print("Simulacion de Puertas Logicas (AND, OR, NOT)")
    print("Ingrese valores binarios (0 o 1)")

    # Se solicita entrada de valores al usuario
    a = int(input("Ingrese el primer valor (0 o 1): "))
    b = int(input("Ingrese el segundo valor (0 o 1): "))

    # Se verifica que los valores ingresados sean validos (0 o 1)
    if a not in [0, 1] or b not in [0, 1]:
        print("Error: Los valores ingresados deben ser 0 o 1.")
        return

    # Operaciones logicas
    resultado_and = a and b
    resultado_or = a or b
    resultado_not_a = not a
    resultado_not_b = not b

    # Mostrar resultados
    print(f"\nResultados:")
    print(f"{a} AND {b} = {resultado_and}")
    print(f"{a} OR {b} = {resultado_or}")
    print(f"NOT {a} = {int(resultado_not_a)}")
    print(f"NOT {b} = {int(resultado_not_b)}")

# Ejecucion de la funcion
simulacion_puertas_logicas()
