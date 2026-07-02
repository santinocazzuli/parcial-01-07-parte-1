#menuu
import inputss 
import archivoss 
import printss 

def ejecutar_menu():
    matriz = None
    while True:
        print("\n1. Cargar Datos\n2. Mostrar Análisis\n3. Salir")
        opc = inputss.pedir_entero_validado("Opción: ", 1, 3)
        if opc == 1:
            matriz = archivoss.cargar_desde_archivo_texto()
        elif opc == 2 and matriz:
            printss.mostrar_analisis(matriz)
        elif opc == 3:
            break