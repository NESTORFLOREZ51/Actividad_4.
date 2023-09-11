from pymongo.mongo_client import MongoClient
# Biblioteca Python usada pa interactuar con MongoDb

#CONEXIÓN
def conexion():
    uri = "mongodb+srv://cagomezj:1234@cluster0.cgumkrz.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    return MongoClient(uri)
# se hace una instalacion de clase "MongoClient"

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos():
    # se define la funcion 
    client = conexion()
    # se asigna  el resultado a la la funcion conexion.
    db = client.actividad4.data_real
    # se asigna el resultado de una funcion llamada conexion
    data_list = []#seasigna la lista vacia
    for data_real_bd in db.find(): # se utiliza para iterar de los resultados la base de datos
        data_list.append(data_real_bd) # se agrega el elemento
    return data_list # se devuelven valoresdesde la funcion

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""