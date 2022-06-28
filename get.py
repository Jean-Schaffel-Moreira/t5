from time import sleep
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:2700/")
mydb = myclient["dbsensor"]
mycol = mydb["sensordados"]

data = mycol.find()
while True:
    data = mycol.find_one()
    print(data)
    sleep(1)

