#inputss
def pedir_entero_validado(mensaje, minimo, maximo):
    while True:
        entrada = input(mensaje)
        es_valido = True
        if len(entrada) == 0: es_valido = False
        for char in entrada:
            if char not in "0123456789": es_valido = False
        
        if es_valido:
            valor = int(entrada)
            if minimo <= valor <= maximo:
                return valor
        print(f"Error: Ingrese un valor entre {minimo} y {maximo}.")