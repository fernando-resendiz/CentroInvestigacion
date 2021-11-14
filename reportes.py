import librerias as lb

tc = ' '

def lista_cientificos():
    lb.clear()
    test = "{:5s}    {:15s}   {:15s}   {:15s}   {:10s}   {:30s}".format(tc, tc, tc, tc, tc, tc)
    print("|" + "="*len(test) + "|")
    print("|    LISTA CIENTIFICOS")
    print("|" + "="*len(test) + "|")
    query = "SELECT * FROM cientificos"
    cone_bd = lb.conectar_bd()
    cursor = cone_bd.cursor()
    x =  cursor.execute(query)
    if x == 0:
        print("Error, no hay cientificos en la base de datos.")
    else:
        print("|" + "="*len(test) + "|")
        print("|NUMERO   NOMBRE            AP PATERNO        AP MATERNO        TELEFONO     CORREO")
        print("|" + "="*len(test) + "|")
        for x in cursor.fetchall():
            print("|{:5s}    {:15s}   {:15s}   {:15s}   {:10s}   {:30s}|".format(x[0], x[1], x[2], x[3], x[4], x[5]))
        print("|" + "="*len(test) + "|")
    cone_bd.close()
    lb.pause()

def lista_proyectos():
    lb.clear()
    test = "{:5s}    {:15s}   {:15s}   {:40s}       {:5s}        ".format(tc, tc, tc, tc, tc)
    print("|" + "="*len(test) + "|")
    print("|    LISTA PROYECTOS")
    print("|" + "="*len(test) + "|")
    query = "SELECT * FROM proyectos"
    cone_bd = lb.conectar_bd()
    cursor = cone_bd.cursor()
    x =  cursor.execute(query)
    if x == 0:
        print("Error, no hay proyectos en la base de datos.")
    else:
        print("|" + "="*len(test) + "|")
        print("|NUMERO   NOMBRE            AREA              DESCRIPCION                                NUMERO CIENTIFICO")
        print("|" + "="*len(test) + "|")
        for x in cursor.fetchall():
            descripcion = lb.split_by_char(x[3], 40)
            i = 0
            while i < len(descripcion)-1:
                print("|{:5s}    {:15s}   {:15s}   {:40s}       {:5s}        |".format(tc, tc, tc, descripcion[i], tc))
                i = i + 1
            print("|{:5s}    {:15s}   {:15s}   {:40s}       {:5s}        |".format(x[0], x[1], x[2], descripcion[-1], x[4]))
            print("|" + " "*len(test) + "|")
        print("|" + "="*len(test) + "|")
    cone_bd.close()
    lb.pause()

def lista_proyectos_area():
    lb.clear()
    test = "{:5s}    {:15s}   {:15s}   {:40s}       {:5s}        ".format(tc, tc, tc, tc, tc)
    print("|" + "="*len(test) + "|")
    print("|    LISTA PROYECTOS POR AREA")
    print("|" + "="*len(test) + "|")
    area = lb.pide_cadena(1, 15, "Ingrese el area a buscar : ")
    query = "SELECT * FROM proyectos WHERE area_pro='"+area+"'"
    cone_bd = lb.conectar_bd()
    cursor = cone_bd.cursor()
    x =  cursor.execute(query)
    if x == 0:
        print("Error, no hay proyectos en la base de datos con el area especificado.")
    else:
        print("|" + "="*len(test) + "|")
        print("|NUMERO   NOMBRE            AREA              DESCRIPCION                                NUMERO CIENTIFICO")
        print("|" + "="*len(test) + "|")
        for x in cursor.fetchall():
            descripcion = lb.split_by_char(x[3], 40)
            i = 0
            while i < len(descripcion)-1:
                print("|{:5s}    {:15s}   {:15s}   {:40s}       {:5s}        |".format(tc, tc, tc, descripcion[i], tc))
                i = i + 1
            print("|{:5s}    {:15s}   {:15s}   {:40s}       {:5s}        |".format(x[0], x[1], x[2], descripcion[-1], x[4]))
            print("|" + " "*len(test) + "|")
        print("|" + "="*len(test) + "|")
    cone_bd.close()
    lb.pause()

def menu_reportes():
    while True:
        lb.clear()
        print("|===============================================|")
        print("|                 MENU REPORTES                 |")
        print("|===============================================|")
        print("|1) Lista de científicos                        |")
        print("|2) Lista de proyectos                          |")
        print("|3) Lista de proyectos por area                 |")
        print("|4) Lista de cientificos por area               |")
        print("|5) Lista de proyectos asignados a un cientifico|")
        print("|6) Terminar                                    |")
        print("|===============================================|")
        op = lb.pide_entero(0,6,"Indique la opción deseada: ")
        
        if op == 1:
            lista_cientificos()
        elif op == 2:
            lista_proyectos()
        elif op == 3:
            lista_proyectos_area()
        elif op == 4:
            continue
        elif op == 5:
            continue
        elif op == 6:
            break
        else:
            lb.error('Opción no válida.')
    return