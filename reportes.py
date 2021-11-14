import librerias as lb

def menu_reportes():
    while True:
        lb.clear()
        print("|===============================================|")
        print("|     MENU REPORTES                             |")
        print("|===============================================|")
        print("|1) Lista de científicos                        |")
        print("|2) Lista de proyectos                          |")
        print("|3) Lista de proyectos por area                 |")
        print("|4) Lista de cientificos por area               |")
        print("|5) Lista de proyectos asignados a un cientifico|")
        print("|6) Terminar                                    |")
        print("|===============================================|")
        op = lb.pide_entero(0,5,"Indique la opción deseada: ")
        
        if op == 1:
            continue
        elif op == 2:
            continue
        elif op == 3:
            continue
        elif op == 4:
            continue
        elif op == 5:
            continue
        elif op == 6:
            break
        else:
            lb.error('Opción no válida.')
    return