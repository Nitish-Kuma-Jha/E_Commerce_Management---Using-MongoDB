from pymongo import MongoClient
client=MongoClient("mongodb://localhost:27017/First_database")

db = client["First_database"]
collection_1=db["students"]
"""
stu={"name":"Amit","age":20,"course":"MongoDB"}
collection_1.insert_one(stu)
print("Data inserted successfully")
stu=[{"name":"Rahul","age":22,"course":"Python"},
      {"name":"Sneha","age":21,"course":"Java"},{"name":"Anjali","age":23,"course":"C++"},{"name":"Vikram","age":24,"course":"JavaScript"}]
collection_1.insert_many(stu)
print("Multiple data inserted successfully")

for i in collection_1.find():
    print(i)
print("Data fetched successfully")

collection_1.update_one({"name":"Amit"},{"$set":{"course":"Data Science"}})
print("Data updated successfully")
collection_1.update_many({"course":"Data Science"},{"$set":{"course":"Introduction to Data Science"}})
print("Multiple data updated successfully")
for i in collection_1.find():
    print(i)
print("Data fetched successfully")
"""
for i in collection_1.find().sort("age",1).limit(3):
    print(i)