#funcioness
def inicializar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = [0] * columnas
        matriz += [fila]
    return matriz

def parsear_linea_csv(linea):
    lista = []
    temp = ""
    for char in linea:
        if char == "," or char == "\n" or char == "\r":
            if len(temp) > 0:
                lista += [temp]
                temp = ""
        else:
            temp += char
    if len(temp) > 0: lista += [temp]
    return lista