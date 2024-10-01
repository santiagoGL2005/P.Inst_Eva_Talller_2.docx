def solicitar_numeros():
    numeros = []

    while len(numeros) < 3:
        try:
            num = int(input(f"Ingrese el número {len(numeros) + 1}: "))

            if num in numeros:
                print("Ingrese un número diferente.")
            else:
                numeros.append(num)

        except ValueError:
            print("Ingrese un número entero válido.")

    return numeros

def analizar_numeros(numeros):
    # Determinar el mayor y el menor
    mayor = max(numeros)
    menor = min(numeros)

    # Calcular suma y promedio
    suma = sum(numeros)
    promedio = suma / 3

    # Identificar pares e impares
    pares = [num for num in numeros if num % 2 == 0]
    impares = [num for num in numeros if num % 2 != 0]

    # Determinar si hay más pares o impares
    if len(pares) > len(impares):
        mas = "Hay más números pares."
    elif len(impares) > len(pares):
        mas = "Hay más números impares."
    else:
        mas = "Hay la misma cantidad de números pares e impares."

    return mayor, menor, suma, promedio, pares, impares, mas

def mostrar_resumen(mayor, menor, suma, promedio, pares, impares, mas):
    print("\n--- Resumen del análisis ---")
    print(f"El número mayor es: {mayor}")
    print(f"El número menor es: {menor}")
    print(f"La suma de los números es: {suma}")
    print(f"El promedio de los números es: {promedio:.2f}")

    print(f"Números pares: {pares if pares else 'No hay números pares'}")
    print(f"Números impares: {impares if impares else 'No hay números impares'}")

    print(mas)

# Programa principal
numeros = solicitar_numeros()
mayor, menor, suma, promedio, pares, impares, mas = analizar_numeros(numeros)
mostrar_resumen(mayor, menor, suma, promedio, pares, impares, mas)