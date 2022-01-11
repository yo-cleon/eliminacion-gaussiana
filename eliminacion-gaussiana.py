# La llamada ELIMINACIÓN GAUSSIANA CON PIVOTAJE PARCIAL ESCALADO utiliza un factor de escalado para identificar
# el número más grande de cada fila. De esta forma se eligen números cuyo factor de escalado minimiza los errores de
# redondeo en el cálculo de los sistemas de ecuaciones equivalentes.

subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

def recoger_matriz():
    # Recoger las matrices

    # rows, cols = (4, 4)
    # matriz = []
    # for i in range(rows):
    #     col = []
    #     for j in range(cols):
    #         elemento = "a"+str(i+1)+str(j+1)
    #         print("Introduce el elemento " + elemento.translate(subscript))
    #         num = input()
    #         col.append(num)
    #     matriz.append(col)
    # print(matriz)
    matriz = [['2', '-6', '10', '-42'], ['-5', '4', '-5', '82'], ['10', '2', '3', '122'], ['0', '0', '0', '0']]
    return matriz


def imprimir_matriz(matriz):
    for linea in matriz:
        for d in linea:
            # print(('%.2f' % float(d)).rstrip('0').rstrip('.'), end=", ")
            print(d, end=", ")
            print("\b\b\t\t\t", end=" ")
        print()


def pivoteo_matriz(mtrz, i):
    pivote = '%.2f' % 0
    pos = 0
    for l in mtrz[i:4]:
        if abs(float(l[i])) > abs(float(pivote)):
            pivote = l[i]
            pos += 1
    elemento = "a" + str(i+1) + str(i+1)
    print(" Elemento  " + elemento.translate(subscript) + ", el pivote de la columna " + str(i+1) + " es " + ('%.2f' % float(pivote)).rstrip('0').rstrip('.'))
    aux = mtrz[i+pos-1]
    mtrz.remove(mtrz[i+pos-1])
    mtrz.insert(i, aux)
    # imprimir_matriz(mtrz)
    return(mtrz)


def eliminacion_gaussiana(matriz, i):
    for k in range(i+1,4):
        # Se anulan los valores por debajo del pivote aplicando la siguiente fórmula
        # Fn+1 - a(n+1)i/ani * Fn
        pivote = matriz[i][i]
        aux = float(matriz[k][i]) / float(pivote)
        for j in range (i,4):
            matriz[k][j] = str(float(matriz[k][j]) - (aux * float(matriz[i][j])))
    return(matriz)

# Función principal.
if __name__ == '__main__':
    matriz = recoger_matriz()
    print("La matriz INICIAL es la siguiente:")
    imprimir_matriz(matriz)
    print()
    row = 0
    for i in range(3):
        print("Ordenando la matriz según la columna ", i+1)
        # Antes de realizar la eliminación, se realiza el pivoteo
        matriz = pivoteo_matriz(matriz, i)
        # Una vez realizado el pivoteo, se aplica la eliminación gaussiana
        matriz = eliminacion_gaussiana(matriz, i)
        imprimir_matriz(matriz)
    print()
    print("La matriz FINAL ordenada es la siguiente:")
    imprimir_matriz(matriz)