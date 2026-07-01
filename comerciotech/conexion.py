from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017/")

db = cliente["comerciotech"]

clientes = db["clientes"]
pedidos = db["pedidos"]
productos = db["productos"]