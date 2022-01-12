# La llamada ELIMINACIÓN GAUSSIANA CON PIVOTAJE PARCIAL ESCALADO utiliza un factor de escalado para identificar
# el número más grande de cada fila. De esta forma se eligen números cuyo factor de escalado minimiza los errores de
# redondeo en el cálculo de los sistemas de ecuaciones equivalentes.

# Función para mostrar subíndices
subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

# Función para solicitar al usuario la introducción de los elementos de la matriz
def recoger_matriz():
    rows, cols = (4, 4)
    matriz = []
    for i in range(rows):
        col = []
        for j in range(cols):
            elemento = "a"+str(i+1)+str(j+1)
            num = input("Introduce el elemento {}: ".format(elemento.translate(subscript)))
            if num == '':
                num = 0
            col.append(num)
        matriz.append(col)
    return matriz

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for linea in matriz:
        for d in linea:
            if d == '-0.00':
                d= '0.00'
            print('%.2f' % float(d), end=", ")
            print("\b\b\t\t\t", end=" ")
        print()

# Función para buscar los pivotes de cada línea: antes de empezar cada etapa i, se realizará
# una búsqueda entre los elementos de la columna y se escogerá aquel de mayor valor absoluto,
# intercambiando a continuación las filas que determinan ese elemento y la i.
def pivoteo_matriz(mtrz, i):
    pivote = '%.2f' % 0
    aux = ''
    for l in mtrz[i:4]:
        if abs(float(l[i])) > abs(float(pivote)):
            pivote = l[i]
            aux = l
    # Si el pivote de una columna es igual a 0, puede generar errores,
    # ya que se origina una división entre cero
    if pivote == '0.00':
        print("La matriz no tiene solución")
        exit(0)
    elemento = "a" + str(i+1) + str(i+1)
    print(" Elemento  " + elemento.translate(subscript) + ", el pivote de la columna " + str(i+1) + " es " +
          ('%.2f' % float(pivote)).rstrip('0').rstrip('.'))
    mtrz.remove(aux)
    mtrz.insert(i, aux)
    return(mtrz)

# Reducción a cero de los elementos inferiores al pivote: Una vez realizada la permutación de las filas,
# se anulan los valores por debajo del pivote, multiplicando la fila de pivote por una cierta constante
# y agregándola a una fila debajo del pivote. En este caso, realizamos la siguiente operación:
# Fn+1 = Fn+1 - aji/aii * Fn
def reduccion_a_cero(matriz, i):
    for j in range(i+1,4):
        pivote = matriz[i][i]
        constante = float(matriz[j][i]) / float(pivote)
        for k in range (i,4):
            matriz[j][k] = float(matriz[j][k]) - (constante * float(matriz[i][k]))
    return(matriz)

# Función principal de la aplicación.
if __name__ == '__main__':
    matriz = recoger_matriz()
    print()
    print("La matriz INICIAL es la siguiente:")
    imprimir_matriz(matriz)
    print()
    row = 0
    for i in range(3):
        print("Ordenando la matriz según la columna ", i+1)
        # Antes de realizar la eliminación, se realiza el pivoteo
        matriz = pivoteo_matriz(matriz, i)
        # Una vez realizado el pivoteo, se realiza la reducción a cero de la columna
        matriz = reduccion_a_cero(matriz, i)
        imprimir_matriz(matriz)
    print()
    print("La matriz FINAL ordenada es la siguiente:")
    imprimir_matriz(matriz)