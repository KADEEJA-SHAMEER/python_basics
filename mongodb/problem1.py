import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient["task1"]

mycol = mydb["students"]

mydict=[{"_id":"205","name":"kadeeja","address":"chennoth","age":21},{"_id":209,"name":"usman"}]
x = mycol.insert_many(mydict)
print(x)

# department,doctor=department_id,register,booking