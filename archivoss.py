#archivoss
import funcioness
import os

def cargar_desde_archivo_texto():
    matriz = funcioness.inicializar_matriz(7, 3)
    directorio_script = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(directorio_script, "notas.csv")
    archivo = open(ruta_archivo, "r")
    matriz = funcioness.inicializar_matriz(7, 3)
    archivo = open("notas.csv", "r")
    fila = 0
    for linea in archivo:
        if "trimestre" in linea: continue 
        datos = funcioness.parsear_linea_csv(linea)
        if len(datos) >= 3:
            for col in range(3):
                matriz[fila][col] = int(datos[col])
        fila += 1
        if fila >= 7: break
    archivo.close()
    return matriz

def guardar_archivo_texto_manual(matriz):
    archivo = open("24-06-2026.csv", "w")
    print("trimestre1,trimestre2,trimestre3", file=archivo)
    for i in range(7):
        linea = str(matriz[i][0]) + "," + str(matriz[i][1]) + "," + str(matriz[i][2])
        print(linea, file=archivo)
    archivo.close()