# =============================================================================
# LABORATORIO PARTE: Procesamiento de Matrices con Datos Fijos
# INSTRUCCIONES:
# 1. NO uses input(). Los datos ya están declarados.
# 2. Usa únicamente listas, ciclos for, condicionales, len().
# 3. Respeta estrictamente la indentación de 4 espacios.
# 4. Reemplaza las variables de entrada con los casos de prueba del enunciado.
# =============================================================================

# ========================
# EJERCICIO 1: Conteo y Suma Condicional en una Matriz
# ========================
print("--- EJERCICIO 1 ---")
matriz_e1 = [
    [5, -2, 0],
    [8, -3, -1],
    [4, 0, 10]
]

positivos = 0
suma_negativos = 0

filas = len(matriz_e1)
columnas = len(matriz_e1[0])

for i in range(filas):
    for j in range(columnas):
        valor = matriz_e1[i][j]
        if valor > 0:
            positivos += 1
        elif valor < 0:
            suma_negativos += valor

# TU CÓDIGO AQUÍ (recorre la matriz con dos ciclos for y aplica condicionales)
# ...

print(positivos, suma_negativos)


# ========================
# EJERCICIO 2: Extracción de Máximos por Fila
# ========================
print("\n--- EJERCICIO 2 ---")
matriz_e2 = [
    [3, 8, 1],
    [10, 2, 5],
    [4, 9, 7]
]

maximos_por_fila = []

filas = len(matriz_e2)
columnas = len(matriz_e2[0])

for i in range(filas):
    max_fila = matriz_e2[i][0]
    for j in range(1, columnas):
        if matriz_e2[i][j] > max_fila:
            max_fila = matriz_e2[i][j]
    maximos_por_fila.append(max_fila)
    
# TU CÓDIGO AQUÍ (recorre cada fila, encuentra el mayor y guárdalo en la lista)
# ...

print(*maximos_por_fila)

#================================================================================