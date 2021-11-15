#A01769960 Carlos Eduardo Jiménez Santiago
#A01769659 Fernando Reséndiz Bautista
#A01367464 Hlib Korzhynskyy

import librerias as lb
import cientificos as mc
import proyectos as mp
import reportes as mr

def menu_principal():
    while True:
        lb.clear()
        print("|==========================|")
        print("|      MENU PRINCIPAL      |")
        print("|==========================|")
        print("|1) Científicos            |")
        print("|2) Proyectos              |")
        print("|3) Reportes               |")
        print("|4) Terminar               |")
        print("|==========================|")
        op = lb.pide_entero(0,4,"Indique la opción deseada: ")
        
        if op == 1:
            mc.menu_cientificos()
        elif op == 2:
            mp.menu_proyectos()
        elif op == 3:
            mr.menu_reportes()
        elif op == 4:
            break
        else:
            lb.error('Opción no válida.')

if __name__ == "__main__":
    menu_principal()
