import os
import pymysql as my

def conectar_bd():
    cone_bd = my.connect(
        host='localhost',
        user='root',
        passwd='',
        database='centroinvestigacion'
    )
    
    return cone_bd

def pide_entero(li, ls, msg):
    while True:
        x = int(input(msg))
        if li<=x<=ls:
            return x
        print('Error valor fuera de rango entre',li,'y',ls,'...')
        input()


def pide_float(li, ls, msg):
    while True:
        x = float(input(msg))
        if li<=x<=ls:
            return x
        print('Error valor fuera de rango entre',li,'y',ls,'...')
        input()

def pause():
    input('Presione [ENTER] para continuar...')

def pide_cadena(li, ls, msg):
    while True:
        string=input(msg)
        strlength=len(string)
        if li<=strlength<=ls:
            return string
        print('Error, la cadena no es de entre',li,'y',ls,'caracteres...')

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def error(msg):
    print(msg)
    input('Presione [ENTER] para continuar...')