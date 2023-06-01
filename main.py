import mysql.connector as db
import json
import os
from tabulate import tabulate
from archivo import *
crear_proveedores()
crear_ubicaciones()
crear_medicamentos()
crear_basedatos()
con = db.connect(host='127.0.0.1', user='informatica1', passwd='bio123', db='informatica', port='3306')
cursor = con.cursor()
while True:
    usuario=input("ingrese su usuario: ")
    contraseña=input("ingrese su contraseña: ")
    if validar_credenciales(usuario, contraseña):
        print("credenciales correctas!")
        while True:
            menu=val_int(print("1 para entrar a medicamentos \n2 para entrar a proveedores "
                               "\n3 para entrar a ubicaciones \n4 para salir"))
            if menu<1 or menu>4:
                print("El numero no esta dentro del rango esperado..")
            else:
                pass
            if menu==1:
                menu1=val_int(print("1 para añadir nuevo medicmento \n2 para actualizar informacion de medicamento"
                                    "\n3 para buscar un medicamento \n4 para ver informacion de algun medicmento \n"
                                    "5 para eliminar un medicamento \n6 para ver tabla \n7 para volver al menu principal"))
                if menu1<1 or menu1>7:
                    print("el numero no esta dentro del rango esperado..")
                if menu1==1:
                    nombre_med=input("ingrese el nombre del medicamento\n")
                    lote_med=val_int(print("ingrese el numero de identificacion"))
                    informacion_med=input("ingrese la informacion del medicamento\n")
                    sql = """INSERT INTO `medicamentos` (`nombre`, `numero_de_lote`, `informacion`) VALUES ('{}', '{}', '{}')""".format(nombre_med, lote_med, informacion_med)
                    cursor.execute(sql)
                    con.commit()
                elif menu1==2:
                    lote_med=val_int(print("ingrese el numero de id del medicamento"))
                    informacion_med=input("ingrese la nueva informacion")
                    sql = """UPDATE `medicamentos` SET `informacion` = '{}' WHERE `numero_de_lote` = {}""".format(informacion_med,lote_med)
                    cursor.execute(sql)
                    con.commit()
                elif menu1==3:
                    lote_med = val_int(print("ingrese el numero de id del medicamento"))
                    sql = """SELECT * FROM `medicamentos` WHERE `numero_de_lote` = '{}'""".format(lote_med)
                    cursor.execute(sql)
                    resultado = cursor.fetchone()
                    if resultado:
                        print(resultado)
                    else:
                        print("No se encontraron resultados.")
                elif menu1==4:
                    lote_med = val_int(print("ingrese el numero de id del medicamento"))
                    sql = """SELECT `informacion` FROM `medicamentos` WHERE `numero_de_lote` = '{}'""".format(lote_med)
                    cursor.execute(sql)
                    resultado = cursor.fetchone()
                    if resultado:
                        campo = resultado[0]
                        print(campo)
                    else:
                        print("No se encontraron resultados.")
                elif menu1==5:
                    lote_med = val_int(print("ingrese el numero de id del medicamento"))
                    sql = """DELETE FROM `medicamentos` WHERE `numero_de_lote` = '{}'""".format(lote_med)
                    cursor.execute(sql)
                    con.commit()
                    print("La fila ha sido eliminada correctamente.")
                elif menu1==6:
                    sql = "SELECT * FROM `medicamentos` "
                    cursor.execute(sql)
                    resultado = cursor.fetchall()
                    if resultado:
                        encabezados = [i[0] for i in cursor.description]
                        tabla = tabulate(resultado, headers=encabezados, tablefmt="pretty")
                        print(tabla)
                    else:
                        print("No se encontraron resultados.")

            if menu==2:
                menu2=val_int(print("1 para ingresar nuevo proveedor \n2 para ver proveedores "
                                    "\n3 para eliminar proveedor \n4 para actualizar datos de un proveedor \n"
                                    "5 para ver datos de proveedor \n6 para ver tabla \n7 para volver al menu principal"))

                if menu2<1 or menu2>7:
                    print("el numero no esta dentro del rango esperado..")
                if menu2==1:
                    nombre_prov = input("ingrese el nombre del proveedor\n")
                    lote_prov = val_int(print("ingrese el numero de identificacion"))
                    informacion_prov = input("ingrese la informacion del proveedor\n")
                    sql = """INSERT INTO `proveedores` (`nombre`, `numero_de_id`, `informacion`) VALUES ('{}', '{}', '{}')""".format(nombre_prov, lote_prov, informacion_prov)
                    cursor.execute(sql)
                    con.commit()
                elif menu2==2:
                    lote_prov = val_int(print("ingrese el numero de id del proveedor"))
                    sql = """SELECT * FROM `proveedores` WHERE `numero_de_id` = '{}'""".format(lote_prov)
                    cursor.execute(sql)
                    resultado = cursor.fetchone()
                    if resultado:
                        print(resultado)
                    else:
                        print("No se encontraron resultados.")
                elif menu2==3:
                    lote_prov = val_int(print("ingrese el numero de id del proveedor"))
                    sql = """DELETE FROM `proveedores` WHERE `numero_de_id` = '{}'""".format(lote_prov)
                    cursor.execute(sql)
                    con.commit()
                    print("La fila ha sido eliminada correctamente.")
                elif menu2==4:
                    lote = val_int(print("ingrese el numero de id del proveedor"))
                    informacion_prov = input("ingrese la nueva informacion")
                    sql = """UPDATE `proveedores` SET `informacion` = '{}' WHERE `numero_de_id` = {}""".format(informacion_prov, lote_prov)
                    cursor.execute(sql)
                    con.commit()
                elif menu2==5:
                    lote_prov = val_int(print("ingrese el numero de id del proveedor"))
                    sql = """SELECT `informacion` FROM `proveedores` WHERE `numero_de_id` = '{}'""".format(lote_prov)
                    cursor.execute(sql)
                    resultado = cursor.fetchone()
                    if resultado:
                        campo = resultado[0]
                        print(campo)
                    else:
                        print("No se encontraron resultados.")
                elif menu2==6:
                    sql = "SELECT * FROM `proveedores` "
                    cursor.execute(sql)
                    resultado = cursor.fetchall()
                    if resultado:
                        encabezados = [i[0] for i in cursor.description]
                        tabla = tabulate(resultado, headers=encabezados, tablefmt="pretty")
                        print(tabla)

            if menu==3:
                menu3 = val_int(print("1 para ingresar nueva ubicacion \n2 para ver ubicacion "
                                      "\n3 para eliminar ubicacion \n4 para actualizar datos de una ubicacion \n"
                                      "5 para ver datos de una ubicacion \n6 para ver tabla \n7 para volver al menu principal"))
                if menu3<1 or menu3>7:
                    print("el numero no esta dentro del rango esperado..")
                if menu3==1:
                    nombre_ub =input("ingrese la direccion")
                    lote_ub = val_int(print("ingrese el numero de identificacion"))
                    informacion_ub = input("ingrese la informacion de la ubicacion\n")
                    sql = """INSERT INTO `ubicaciones` (`direccion`, `numero_de_identificacion`, `informacion`) VALUES ('{}', '{}', '{}')""".format(nombre_ub, lote_ub, informacion_ub)
                    cursor.execute(sql)
                    con.commit()
                elif menu3==2:
                    lote_ub=val_int(print("ingrese el numero de id de la ubicacion"))
                    sql = """SELECT * FROM `ubicaciones` WHERE `numero_de_identificacion` = '{}'""".format(lote_ub)
                    cursor.execute(sql)
                    resultado = cursor.fetchone()
                    if resultado:
                        print(resultado)
                    else:
                        print("No se encontraron resultados.")
                elif menu3==3:
                    lote_ub = val_int(print("ingrese el numero de id de la ubicacion"))
                    sql = """DELETE FROM `ubicaciones` WHERE `numero_de_identificacion` = '{}'""".format(lote_ub)
                    cursor.execute(sql)
                    con.commit()
                    print("La fila ha sido eliminada correctamente.")
                elif menu3==4:
                    lote_ub = val_int(print("ingrese el numero de id de la ubicacion"))
                    informacion_ub = input("ingrese la nueva informacion\n")
                    sql = """UPDATE `ubicaciones` SET `informacion` = '{}' WHERE `numero_de_identificacion` = {}""".format(informacion_ub, lote_ub)
                    cursor.execute(sql)
                    con.commit()
                elif menu3==5:
                    lote = val_int(print("ingrese el numero de id de la ubicacion"))
                    sql = """SELECT `informacion` FROM `ubicaciones` WHERE `numero_de_identificacion` = '{}'""".format(lote_ub)
                    cursor.execute(sql)
                    resultado = cursor.fetchone()
                    if resultado:
                        campo = resultado[0]
                        print(campo)
                    else:
                        print("No se encontraron resultados.")
                elif menu3==6:
                    sql = "SELECT * FROM `ubicaciones` "
                    cursor.execute(sql)
                    resultado = cursor.fetchall()
                    if resultado:
                        encabezados = [i[0] for i in cursor.description]
                        tabla = tabulate(resultado, headers=encabezados, tablefmt="pretty")
                        print(tabla)

            if menu==4:
                break


        break
    else:
        print("credenciales invalidas, intente nuevamente")