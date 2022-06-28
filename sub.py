#!python3

import paho.mqtt.client as mqtt
from datetime import datetime
from pymongo import MongoClient

mongoclient = MongoClient("mongodb://localhost:2700/")
db = mongoclient["dbsensor"]
collection = db["sensordados"]

hora = None
dado = None

def on_connect(client, userdata, flags, rc):
	if rc==0:
		print("Conectado com Sucesso!")
	else:
		print("Falha de Conexão, Codigo: ", rc)

		client.subscribe("sensor/time")
		client.subscribe("sensor/data")

def on_message(client, userdata, msg):
	global hora
	global dado


	if msg.topic == "sensor/time":
		hora = msg.payload.decode()
		return
	else:
		print("Recebido com Sucesso!")
		dado = msg.payload.decode()

	post = {"Hora": hora, "Dado": dado}
	
	collection.insert_one(post)
	print("Repassado com Sucesso! ")

def on_disconnect(client, userdata, flags, rc=0):
	print("Desconectado, Codigo: "+str(rc))


client = mqtt.Client("meu_cliente")
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect
broker="localhost"

client.connect(broker)

	

client.loop_forever()
