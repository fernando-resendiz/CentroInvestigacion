import librerias as lb

def menu_cientificos():
    while True:
        lb.clear()
        print("|==========================|")
        print("|     MENU CIENTIFICOS     |")
        print("|==========================|")
        print("|1) Altas de científicos   |")
        print("|2) Bajas de científicos   |")
        print("|3) Consulta de científicos|")
        print("|4) Cambios de científicos |")
        print("|5) Terminar               |")
        print("|==========================|")
        op = lb.pide_entero(0,5,"Indique la opción deseada: ")
        
        if op == 1:
            break
        elif op == 2:
            break
        elif op == 3:
            break
        elif op == 4:
            break
        elif op == 5:
            break
        else:
            lb.error('Opción no válida.')
    return