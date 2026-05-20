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

```
- Implementar recorridos secuenciales y anidados utilizando ciclos.
```

```
- Manipular matrices bidimensionales mediante indexación directa.
```

```
- Aplicar condicionales y operaciones de comparación sobre estructuras
estáticas.
```

- `Validar la lógica modificando manualmente los datos fijos en el código.` 

```
🎯 NORMAS DE COMPORTAMIENTO Y NOTACIÓN
```

```
- Declaración fija en Python: lista = [1, 2, 3] | matriz = [[1, 2], [3, 4]]
- Obtención de tamaño: len(matriz) → filas | len(matriz[0]) → columnas
```

```
- Ciclos: for i in range(N):
```

```
- Condicionales: if / elif / else (con indentación de 4 espacios)
```

`- Impresión de lista: print(*resultado) → separa elementos con espacios -  RESTRICCIÓN: No utilizar input(). Todos los datos van hardcodeados.` ⛔ `- 🎯 INDENTACIÓN: Python usa 4 espacios por nivel. No existen llaves {}.` 

`--------------------------------------------------------------------------------` 
🟢 `EJERCICIO 1: Conteo y Suma Condicional en una Matriz Enunciado: Dada una matriz fija de números enteros, recorra todos sus elementos y determine:` 

```
1. La cantidad de números positivos (estrictamente mayores a 0).
2. La suma acumulada de los números negativos (estrictamente menores a 0).
Los valores iguales a 0 deben ser ignorados. Imprima ambos resultados en una
sola línea, separados por un espacio.
```

```
🎯 CASOS DE ENTRADA PARA VALIDACIÓN:
| Caso | Declaración en Python
|
|------|------------------------------------------------------------------------
|
| 1    | matriz = [[5, -2, 0], [8, -3, -1], [4, 0, 10]]
|
| 2    | matriz = [[-1, -2], [-3, -4], [-5, -6]]
|
| 3    | matriz = [[7, 7], [7, 7], [7, 7]]
|
| 4    | matriz = [[0, 0, 0], [0, -10, 10], [0, 0, 0]]
|
```

`--------------------------------------------------------------------------------` 

🟡 `EJERCICIO 2: Extracción de Máximos por Fila Enunciado: Dada una matriz fija de enteros de dimensiones F x C, recorra cada fila individualmente, identifique el valor máximo presente en dicha fila y almacene ese máximo en un arreglo unidimensional. Al finalizar, imprima el arreglo resultante, manteniendo el orden original de las filas.` 

```
🎯 CASOS DE ENTRADA PARA VALIDACIÓN:
| Caso | Declaración en Python
|
|------|------------------------------------------------------------------------
|
| 1    | matriz = [[1, 2], [5, 3], [0, 0]]
|
| 2    | matriz = [[-10, -5, -2], [-8, -12, -3]]
|
| 3    | matriz = [[4, 4, 4], [4, 4, 4]]
```

```
|
| 4    | matriz = [[100], [50], [200]]
|
```

- 📋 `INSTRUCCIONES PARA ESTUDIANTES:` 

`1. Cree un bloque independiente por cada ejercicio.` 

`2. Utilice exclusivamente la sintaxis de Python indicada en la guía.` 

`3. No use input(). Copie directamente la declaración de la tabla para probar cada caso.` 

`4. Compare sus resultados impresos con cálculos manuales.` 

`5. El uso de len() es OBLIGATORIO para definir los límites de los ciclos.` 

`6. Entregue un único archivo .py con los 2 ejercicios ejecutables.` 

```
=================================================================================
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
🎯 4. CONDICIONALES
if valor > 0:
    positivos += 1
elif valor < 0:
    suma_neg += valor
```

```
🎯 5. INDENTACIÓN (REGLA DE ORO EN PYTHON)
🎯 Correcto:
for i in range(3):
    if i > 0:
        print("Mayor")
```

```
🎯 Incorrecto:
for i in range(3):
if i > 0:
    print("Error")
```

🖨️� `6. IMPRESIÓN DE LISTAS print(*resultado)  # Desempaqueta: [1, 2, 3] → "1 2 3"` 

```
🎯 7. EJEMPLO PRÁCTICO: RECORRIDO DE MATRICES RECTANGULARES (NO CUADRADAS)
matriz_rect = [
    [10, -2, 0, 5],   # Fila 0 → 4 columnas
    [-3, 8, 1, -4]    # Fila 1 → 4 columnas
]
filas = len(matriz_rect)       # 2
columnas = len(matriz_rect[0]) # 4
for i in range(filas):
    for j in range(columnas):
```

```
        valor = matriz_rect[i][j]
        if valor > 0:
            pass
        elif valor < 0:
            pass
```

```
================================================================================
```

