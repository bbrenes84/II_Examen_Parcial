import os
import sys
sys.path.append(r"C:\Users\Usuario\OneDrive\Documentos\Univalle\2024.1.1.Lenguaje de Programación\ConexiónBD")
from dao import daoConnection
from models import clases as c


os.system('cls')
conex = daoConnection.Connection("localhost", "root", "", "bdregisters")
conex.connect()

def insertarCiudad():
    nombre = input("Nombre Ciudad")
    ciudad = c.City(id, nombre, 1)
    daoCity = daoConnection.DaoCity(conex)
    daoCity.insert(ciudad)

def mostrarCiudad(): 
    daoCity=daoConnection.DaoCity(conex)
    cities = daoCity.get_all()
    for city in cities:
        print(city)

def editarCiudad():
    id=input("Código Ciudad")
    nombre = input("Nombre Ciudad")
    ciudad = c.City(id, nombre, 1)
    daoCity = daoConnection.DaoCity(conex)
    daoCity.update(ciudad)


def borrarCiudad():
    id=input("Código Ciudad")
    daoCity = daoConnection.DaoCity(conex)
    daoCity.delete(id)

def buscarCiudad():
    nombre = input("Nombre Ciudad")
    ciudad = c.City(0, nombre, 1)
    print(ciudad)
    daoCity = daoConnection.DaoCity(conex)
    reg = daoCity.buscar(nombre)
    print(reg)

def buscarCiudadId():
    id = int(input("Id: "))
    daoCity = daoConnection.DaoCity(conex)
    reg = daoCity.get_by_id(id)
    print(reg)


def Menu():
    print("1. Ingresar Ciudad")
    print("2. Editar Ciudad")
    print("3. Mostrar Ciudad")
    print("4. Eliminar Ciudad")
    print("5. Buscar Ciudad")
    print("6. Salir")

def main():
    opcion = 0
    while(opcion != 6):
        Menu()
        opcion = int(input("Ingrese la opcion\n" ))
        if (opcion == 1 ):
            insertarCiudad()
            os.system("pause")
        elif(opcion == 2):
            editarCiudad()
            os.system("pause")
        elif(opcion == 3):
            mostrarCiudad()
            os.system("pause")
        elif(opcion == 4):
            borrarCiudad()
            os.system("pause")
        elif(opcion == 5):
            buscarCiudad()
            os.system("pause")
        if(opcion == 6):
            print("saliendo del menu")
            break
           
main()
