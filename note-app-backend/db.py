import json
import threading

global database
database = {}
file = "db.json"


def openJsonFile():
    with open(file,"r") as f:
        global database
        database = json.load(f)

def changeData(key,value):
    database[key] = value
    saveJsonFile()

def deleteData(key):
    del database[key]

def getData(key) -> any:
    return database[key]


def saveJsonFile():
    with open(file,"w") as f:
        json.dump(database,f)
