# -*- coding: utf-8 -*-
'''
If the file is't exists create puntajes.csv
if the file exists save the data
'''
try:
    import pathlib
    import csv
except ImportError as error:
    print(error)
archivo = pathlib.Path('puntajes.csv')


def guardar_registro(nombre, tiempo, movimientos):
    '''save the data in puntajes.csv
    '''
    if archivo.exists():
        with open(archivo, 'a', newline='', encoding='utf-8') as csvarchivo:
            grabararchivo = csv.writer(csvarchivo, quotechar=',')
            grabararchivo.writerow([nombre, tiempo, movimientos])


def validar_archivo():
    '''create the file puntajes.csv and after save the data
    '''
    if not archivo.exists():
        with open(archivo, 'w', newline='') as csvarchivo:
            columnas = ['----NAME----', '---TIME---', '----MOVES----']
            grabararchivo = csv.DictWriter(csvarchivo, fieldnames=columnas)
            grabararchivo.writeheader()


def buscar_registro(nombre, tiempo, movimientos):
    '''Verify if the file puntajes.csv exists
    '''
    if not archivo.exists():
        validar_archivo()
    guardar_registro(nombre, tiempo, movimientos)
