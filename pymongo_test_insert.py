from pymongo_get_database import get_database
import json

dbname = get_database()
filepath = '/Users/felipe/Desktop/MONGO/data.json'

collection_name = dbname["JSON_DATA"]

with open(filepath) as f:
    data = json.load(f)
'''item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}

item_2 = {
  "_id" : "U1IT00002",
  "item_name" : "Egg",
  "category" : "food",
  "quantity" : 12,
  "price" : 36,
  "item_description" : "brown country eggs"
}'''
collection_name.insert_one(data)