import librerias as lb

def altas_proyectos():
    lb.clear()
    print("|========================|")
    print("|   ALTAS DE PROYECTOS   |")
    print("|========================|")
    vid=lb.pide_id(          "Indique el ID del proyecto [5 dígitos] : ")
    vnm=lb.pide_cadena(1,15, "Indique el nombre del proyecto         : ")
    var=lb.pide_cadena(1,15, "Indique el área a la que corresponde   : ")
    vds=lb.pide_cadena(1,200,"Agregue una descripción al proyecto    : ")
    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    x=0
    while x==0:
        vci=lb.pide_id(          "Indique la ID del empleado a cargo     : ")
        query="SELECT * FROM cientificos WHERE id_ci='"+vci+"'"
        x=cursor.execute(query)
        if x==0:
            print("La ID del empleado no existe en la base de datos")
        else:
            da_cin=cursor.fetchone()
            print("Nombre : "+da_cin[1]+" "+da_cin[2]+" "+da_cin[3])
            query="INSERT INTO proyectos VALUES('"+vid+"','"+vnm+"','"+var+"','"+vds+"','"+vci+"')"
            seguro=lb.pide_cadena(1,1,"Los datos introducidos son correctos? [Y/N] : ")
            seguro=seguro.upper()
            if seguro=="Y":
                try:
                    x=cursor.execute(query)
                except:
                    x=0

                if x==0:
                    print("ERROR, La ID del proyecto se duplica en la base de datos")
                    break
                else:
                    cone_bd.commit()
                    cone_bd.close()
                    print("Los datos se grabaron correctamente")
            else:
                print("Se ha cancelado la operación")
    lb.pause()

def bajas_proyectos():
    lb.clear()
    print("|========================|")
    print("|   BAJAS DE PROYECTOS   |")
    print("|========================|")
    vid=lb.pide_id("Indica la ID del proyecto a DAR DE BAJA [5 dígitos]: ")
    query = "DELETE FROM `proyectos` WHERE `proyectos`.`id_pro`='"+vid+"'"
    seguro=lb.pide_cadena(1,1,"¿Seguro que deseas dar de baja éste proyecto? [Y/N] : ")
    seguro=seguro.upper()
    if seguro=="Y":
        cone_bd=lb.conectar_bd()
        cursor=cone_bd.cursor()
        x=cursor.execute(query)

        if x==0:
            print("Error, la ID del proyecto no se encuentra en la base de datos")
        else:
            cone_bd.commit()
            print("El registro ha sido dado de baja")
        cone_bd.close()
    else:
        print("Se ha cancelado la operación")
    lb.pause()

def consulta_proyectos():
    lb.clear()
    print("|========================|")
    print("|   CONSULTA PROYECTOS   |")
    print("|========================|")
    vid=lb.pide_id("Indica la ID del proyecto a buscar [5 dígitos]: ")
    query="SELECT id_pro, nombre_pro, area_pro, id_ci_pro, descripcion_pro, "
    query+="id_ci, nombre_ci, am_ci, ap_ci FROM proyectos, cientificos WHERE "
    query+="id_pro='"+vid+"' and id_ci_pro=id_ci"
    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    x=cursor.execute(query)
    if x==0:
        print("Error, la ID del proyecto no se encuentra en la base de datos")
    else:
        datos_pro=cursor.fetchone()
        nomci=datos_pro[6]+" "+datos_pro[7]+" "+datos_pro[8]
        print("=================================================")
        print("Nombre del proyecto   :",datos_pro[1])
        print("Área de investigación :",datos_pro[2])
        print("ID del encargado      :",datos_pro[3])
        print("Nombre del encargado  :",nomci)
        print("Descripción           :",datos_pro[4])
        print("=================================================")
        print()
    cone_bd.close()
    lb.pause()

def cambios_proyectos():
    lb.clear()
    print("|========================|")
    print("|  CAMBIOS DE PROYECTOS  |")
    print("|========================|")
    vid=lb.pide_id(    "Indique el ID del proyecto al que se hará el cambio : ")
    cone_bd=lb.conectar_bd()
    cursor=cone_bd.cursor()
    x=0
    while x==0:
        vci=lb.pide_id("Indique la ID del nuevo empleado a cargo            : ")
        query="SELECT * FROM cientificos WHERE id_ci='"+vci+"'"
        x=cursor.execute(query)
        if x==0:
            print("La ID del empleado no existe en la base de datos")
        else:
            da_cin=cursor.fetchone()
            print("Nombre : "+da_cin[1]+" "+da_cin[2]+" "+da_cin[3])
            query="UPDATE proyectos SET id_ci_pro='"+vci+"' WHERE id_pro='"+vid+"'"
            y=cursor.execute(query)
            if y==0:
                query="SELECT * FROM proyectos WHERE id_pro='"+vid+"'"
                z=cursor.execute(query)
                comp=cursor.fetchone()
                try:
                    if comp[4]==vci:
                        print("Error, no se puede realizar el cambio")
                        print("El científico indicado ya es el encargado de éste proyecto")
                except:
                    print("Error, la ID del proyecto no se encuentra en la base de datos")
            else:
                cone_bd.commit()
                print("El cambio se ha realizado exitosamente")
            cone_bd.close()
    lb.pause()
    

def menu_proyectos():
    while True:
        lb.clear()
        print("|========================|")
        print("|     MENU PROYECTOS     |")
        print("|========================|")
        print("|1) Altas de proyectos   |")
        print("|2) Bajas de proyectos   |")
        print("|3) Consulta de proyectos|")
        print("|4) Cambios de proyectos |")
        print("|5) Terminar             |")
        print("|==========================|")
        op = lb.pide_entero(0,5,"Indique la opción deseada: ")
        
        if op == 1:
            altas_proyectos()
        elif op == 2:
            bajas_proyectos()
        elif op == 3:
            consulta_proyectos()
        elif op == 4:
            cambios_proyectos()
        elif op == 5:
            break
        else:
            lb.error('Opción no válida.')
    return
