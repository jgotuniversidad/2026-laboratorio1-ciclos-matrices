# =============================================================================
# LABORATORIO PARTE 2: Procesamiento de Matrices con Datos Fijos
# INSTRUCCIONES:
# 1. NO uses input(). Los datos ya están declarados.
# 2. Usa únicamente listas, ciclos for, condicionales, len() y división entera (//).
# 3. Respeta estrictamente la indentación de 4 espacios.
# 4. Reemplaza las variables de entrada con los casos de prueba del enunciado.
# =============================================================================

# ========================
# EJERCICIO 1: Suma de la Diagonal Principal
# ========================
print("--- EJERCICIO 1 ---")
matriz_e1 = [
    [2, 0, 1],
    [4, 3, 2],
    [1, 5, 6]
]

suma_diagonal = 0
filas = len(matriz_e1)

for i in range(filas):
    suma_diagonal += matriz_e1[i][i]

# TU CÓDIGO AQUÍ (recorre solo donde índice de fila == índice de columna)
# ...

print(suma_diagonal)


# ========================
# EJERCICIO 2: Promedio Entero por Columna
# ========================
print("\n--- EJERCICIO 2 ---")
matriz_e2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

promedios_por_columna = []
filas = len(matriz_e2)
columnas = len(matriz_e2[0])

for j in range(columnas):
    suma_col = 0
    for i in range(filas):
        suma_col += matriz_e2[i][j]
    promedios_por_columna.append(suma_col // filas)


# TU CÓDIGO AQUÍ (recorre por columnas primero, suma, divide con // y guarda)
# ...

print(*promedios_por_columna)

#================================================================================