```
================================================================================
LABORATORIO: ARREGLOS, CICLOS Y MATRICES
================================================================================
```

```
[PARTE 1: ENUNCIADO DEL LABORATORIO]
```

```
🎯 OBJETIVOS
```

- `Implementar recorridos diagonales y por columnas utilizando ciclos.` 

- `Manipular matrices bidimensionales y generar arreglos de resultados.` 

```
- Aplicar operaciones aritméticas (suma, división entera) sobre estructuras
estáticas.
```

- `Validar la lógica modificando manualmente los datos fijos en el código.` 

```
🎯 NORMAS DE COMPORTAMIENTO Y NOTACIÓN
```

- `Declaración fija en Python: lista = [1, 2, 3] | matriz = [[1, 2], [3, 4]]` 

```
- Obtención de tamaño: len(matriz) → filas | len(matriz[0]) → columnas
```

- `Ciclos: for i in range(N):` 

- `División entera: suma // filas (descarta decimales)` 

- `Impresión de lista: print(*resultado) → separa elementos con espacios` 

- `RESTRICCIÓN: No utilizar input(). Todos los datos van hardcodeados.` ⛔ `- 🎯 INDENTACIÓN: Python usa 4 espacios por nivel. No existen llaves {}.` 

`--------------------------------------------------------------------------------` 🟢 `EJERCICIO 1: Suma de la Diagonal Principal en Matriz Cuadrada Enunciado:` 

```
Dada una matriz fija de enteros con dimensiones N x N (siempre cuadrada),
recorra únicamente los elementos de la diagonal principal (donde el índice de
fila coincide con el índice de columna) y calcule su suma total. Imprima el
resultado numérico.
```

```
🎯 CASOS DE ENTRADA PARA VALIDACIÓN:
```

```
| Caso | Declaración en Python
|
|------|------------------------------------------------------------------------
|
| 1    | matriz = [[5, 0], [0, 5]]
|
| 2    | matriz = [[-3, 2, 1], [4, 0, 5], [6, 7, -1]]
|
| 3    | matriz = [[9]]
|
| 4    | matriz = [[1, 0, 0, 0], [0, 2, 0, 0], [0, 0, 3, 0], [0, 0, 0, 4]]
|
```

`--------------------------------------------------------------------------------` 🟡 `EJERCICIO 2: Promedio Entero por Columna Enunciado:` 

```
Dada una matriz fija de enteros de dimensiones F x C, calcule el promedio entero
de cada columna. Para hacerlo, sume todos los elementos de la columna y divida
entre el número total de filas F utilizando división entera (//, descartando
decimales). Almacene cada promedio en un arreglo unidimensional e imprímalo.
```

```
🎯 CASOS DE ENTRADA PARA VALIDACIÓN:
```

```
| Caso | Declaración en Python
|
|------|------------------------------------------------------------------------
|
| 1    | matriz = [[10, 20], [30, 40], [50, 60]]
|
| 2    | matriz = [[0, 1, 2], [1, 2, 3]]
|
| 3    | matriz = [[-2, 5], [3, 0], [1, -1]]
|
| 4    | matriz = [[7, 8, 9, 10], [1, 2, 3, 4]]
```

```
|
```

📋 `INSTRUCCIONES PARA ESTUDIANTES:` 

`1. Cree un bloque independiente por cada ejercicio.` 

`2. Utilice exclusivamente la sintaxis de Python indicada en la guía.` 

`3. No use input(). Copie directamente la declaración de la tabla para probar cada caso.` 

`4. Compare sus resultados impresos con cálculos manuales.` 

`5. El uso de len() es OBLIGATORIO para definir los límites de los ciclos.` 

`6. Entregue un único archivo .py con los 2 ejercicios ejecutables.` 

```
================================================================================
```

```
[PARTE 2: GUÍA RÁPIDA DE PYTHON]
```

📦 `1. DECLARACIÓN DE MATRICES (DATOS FIJOS) matriz = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]` 

```
🎯 2. OBTENER DIMENSIONES CON len()
filas = len(matriz)       # Número de filas
columnas = len(matriz[0]) # Número de columnas (asume matriz rectangular válida)
```

```
🎯 3. CICLOS for Y range()
# Recorrer matriz 2D (FILA por FILA)
for i in range(filas):
    for j in range(columnas):
        print(matriz[i][j])
```

```
# Recorrer matriz 2D (COLUMNA por COLUMNA)
for j in range(columnas):
    for i in range(filas):
        print(matriz[i][j])
```

```
🎯 4. CONDICIONALES Y OPERACIONES
if valor > 0:
    positivos += 1
🎯 5. INDENTACIÓN (REGLA DE ORO EN PYTHON)
🎯 Correcto:
for i in range(3):
    if i > 0:
        print("Mayor")
🎯 Incorrecto:
for i in range(3):
if i > 0:
    print("Error")
```

🖨️� `6. IMPRESIÓN DE LISTAS Y DIVISIÓN ENTERA print(*resultado)  # Desempaqueta: [1, 2, 3] → "1 2 3" promedio = suma // filas  # División entera` 

```
🎯 7. EJEMPLO PRÁCTICO: RECORRIDO DE MATRICES RECTANGULARES (NO CUADRADAS)
matriz_rect = [
    [10, -2, 0, 5],   # Fila 0 → 4 columnas
    [-3, 8, 1, -4]    # Fila 1 → 4 columnas
]
filas = len(matriz_rect)       # 2
columnas = len(matriz_rect[0]) # 4
```

```
for i in range(filas):
    for j in range(columnas):
        valor = matriz_rect[i][j]
        # Lógica de procesamiento...
```

```
================================================================================
```

