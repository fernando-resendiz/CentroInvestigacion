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

    if seguro in ['Y', 'S', 'YES', 'SI']:
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

def bajas_cientificos():
    lb.clear()
    print("|==========================|")
    print("|     BAJAS CIENTÍFICOS    |")
    print("|==========================|")
    id_ci = lb.pide_id('Indique el número de empleado que desea eliminar [5 dígitos]: ')
    
    cone_bd = lb.conectar_bd()
    cursor = cone_bd.cursor()
    x = cursor.execute("SELECT * FROM `proyectos` WHERE id_ci_pro='"+id_ci+"'")

    if x != 0: 
        lb.clear()
        print("ERROR, el numero de empleado",id_ci,"no puede ser dado de baja ya que tiene proyectos asignados.")
        lb.pause()
        return
    
    print()
    query = "DELETE FROM `cientificos` WHERE id_ci='"+id_ci+"'"
    print(query)
    print()

    seguro = input("Está seguro de querer elminar [Y/N]: ")
    seguro = seguro.upper()
    print()
    
    if seguro in ['Y', 'S', 'YES', 'SI']:
        x = cursor.execute(query)

        if x == 0:
            print('ERROR, el numero de empleado no existe en la tabla cientificos.')
        else:
            cone_bd.commit()
            print("El registro se ha eliminado correctamente.")
        cone_bd.close()
    else:
        print("La accion de eliminar ha sido cancelada.")
    
    lb.pause()

def consulta_cientificos():
    lb.clear()
    print("|==========================|")
    print("|   CONSULTA CIENTÍFICOS   |")
    print("|==========================|")
    id_ci = lb.pide_id('Indique el número de empleado [5 dígitos]      : ')

    lb.clear()
    query = "SELECT * FROM `cientificos` WHERE id_ci='"+id_ci+"'"
    print(query)
    print()

    cone_bd = lb.conectar_bd()
    cursor  =cone_bd.cursor()
    x = cursor.execute(query)
    if x == 0:
        print("Error, el numero de empleado",id_ci,"no existe en la tabla cientificos.")
    else:
        datos_cientifico = cursor.fetchone()
        print("=================================================")
        print("Nombre           :",datos_cientifico[1])
        print("Apellido Paterno :",datos_cientifico[2])
        print("Apellido Materno :",datos_cientifico[3])
        print("Teléfono         :",datos_cientifico[4])
        print("Correo           :",datos_cientifico[5])
        print("=================================================")
        print()
    cone_bd.close()
    lb.pause()

def cambios_cientificos():
    lb.clear()
    print("|==========================|")
    print("|  CAMBIOS DE CIENTÍFICOS  |")
    print("|==========================|")
    id_ci = lb.pide_id(         'Indique el número de empleado [5 dígitos]          : ')
    tel_ci = lb.pide_telefono(  'Indique el nuevo número telefónico del cientifico  : ')
    correo_ci = lb.pide_correo( 'Indique el nuevo correo electrónico del científico : ')

    print()
    query = "UPDATE cientificos SET tel_ci='"+tel_ci+"', correo_ci='"+correo_ci+"' WHERE id_ci='"+id_ci+"'"
    print(query)
    print()

    seguro = input("Los datos intruducidos son correctos? [Y/N]: ")
    seguro = seguro.upper()
    print()

    if seguro in ['Y', 'S', 'YES', 'SI']:
        cone_bd = lb.conectar_bd()
        cursor  = cone_bd.cursor()
        x = cursor.execute(query)
        if x == 0:
            print("Error, el numero de empleado",id_ci,"no existe en la tabla cientificos.")
        else:
            cone_bd.commit()
            print("El cambio ha sido realizado.")
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
            bajas_cientificos()
        elif op == 3:
            consulta_cientificos()
        elif op == 4:
            cambios_cientificos()
        elif op == 5:
            break
        else:
            lb.error('Opción no válida.')
    return