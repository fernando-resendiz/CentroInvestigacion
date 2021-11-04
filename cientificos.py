import librerias as lb

def altas_cientificos():
    lb.clear()
    print("|==========================|")
    print("|   ALTAS DE CIENTÍFICOS   |")
    print("|==========================|")

    id_ci = lb.pide_id(             'Indique el número de empleado [5 dígitos]      : ')
    nombre_ci = lb.pide_cadena(1,15,'Indique el nombre de pila del científico       : ')
    ap_ci = lb.pide_cadena(1,15,    'Indique el apellido paterno del científico     : ')
    am_ci = lb.pide_cadena(1,15,    'Indique el apellido materno del científico     : ')
    tel_ci = lb.pide_telefono(      'Indique el número telefónico del cientifico    : ')
    correo_ci = lb.pide_correo(     'Indique el correo electrónico del científico   : ')

    print()
    query =  """INSERT INTO `cientificos` (`id_ci`, `nombre_ci`, `ap_ci`, `am_ci`, `tel_ci`, `correo_ci`)
VALUES ('"""+id_ci+"','"+nombre_ci+"','"+ap_ci+"','"+am_ci+"','"+tel_ci+"','"+correo_ci+"')"
    print(query)
    print()
    
    seguro = input("Los datos intruducidos son correctos? [Y/N]: ")
    seguro = seguro.upper()
    print()

    afirmativo = ['Y', 'S', 'YES', 'SI']

    if seguro in afirmativo:
        try:
            cone_bd = lb.conectar_bd()
            cursor  = cone_bd.cursor()
            x = cursor.execute(query)
        except:
            x = 0

        if x == 0:
            lb.clear()
            print('ERROR, el numero de empleado se duplica en la tabla cientificos.')
        else:
            cone_bd.commit()
            print('Los datos fueron grabados correctamente.')
        cone_bd.close()
    else:
        print('La ejecución fue cancelada.')
    
    lb.pause()

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
            altas_cientificos()
        elif op == 2:
            pass
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            break
        else:
            lb.error('Opción no válida.')
    return