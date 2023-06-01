#definicion de funciones primordiales para la eficiencia y estetica del codigo principal
import json
import mysql.connector as db

def val_int(numero):

    '''
    :param numero: necesariamente es un print con la instruccion, esto por comodidad y recursividad en la funcion
    :return: permite continuar si el tipo de dato ingresado es numerico
    '''

    while True:
        try:
            numero=int(input(""))
        except ValueError:
            print("el caracter ingresado no es el esperado, intente nuevamente:")
            continue
        else:
            return numero
            break

def val_str(palabra):

    '''
    :param palabra: necesariamente es un print con la instruccion, esto por comodidad y recursividad en la funcion
    :return: permite continuar si el tipo de dato ingresado es alfabetico
    '''

    while True:
        palabra=input("")
        if palabra.isalpha():
            break
        else:
            print("el caracter ingresado no es el esperado, intente nuevamente:")
            continue

def validar_credenciales(usuario,contraseña):
    '''

    :param usuario: usuario registrado en base de datos
    :param contraseña: contraseña regsitrad en base de datos
    :return: ingresa al programa si esta registrado, de lo contrario solicita de nuevo ambos datos
    '''
    with open("data.json", "r") as file:
        users = json.load(file)
        claves = list(users.keys())
        valores = list(users.values())
        for k in range(len(valores)):
            if valores[k]["user"] == usuario and valores[k]["password"] == contraseña:
                return True
            else:
                continue
con = db.connect(host='127.0.0.1', user='informatica1', passwd='bio123', db='informatica', port='3306')
cursor = con.cursor()
#las siguientes funciones crean tablas en nuestra base de datos siempre y cuando no existan
def crear_basedatos():
    nombre='informatica'
    sql_nombre=f"CREATE DATABASE IF NOT EXISTS {nombre}"
    cursor.execute(sql_nombre)
def crear_medicamentos():
    med = '''CREATE TABLE IF NOT EXISTS medicamentos (nombre VARCHAR(100) NOT NULL, numero_de_lote INT NOT NULL, informacion VARCHAR(500) NOT NULL)'''
    cursor.execute(med)
    con.commit()

def crear_proveedores():
    prov = '''CREATE TABLE IF NOT EXISTS proveedores (nombre VARCHAR(100) NOT NULL, numero_de_id INT NOT NULL , informacion VARCHAR(500) NOT NULL)'''
    cursor.execute(prov)
    con.commit()

def crear_ubicaciones():
    ubi = '''CREATE TABLE IF NOT EXISTS ubicaciones (direccion VARCHAR(100) NOT NULL, numero_de_identificacion INT NOT NULL , informacion VARCHAR(500) NOT NULL)'''
    cursor.execute(ubi)
    con.commit()


