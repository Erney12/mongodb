from pymongo import MongoClient

MONGO_URI="mongodb://mongo"

client=MongoClient(MONGO_URI)

db=client["teststore"]
collection=db["products"]
collection.insert_one({"name":"mause", "prexe":2399})