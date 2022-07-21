import pymongo


client = pymongo.MongoClient("mongodb+srv://Akshay:Ram12345@akshay.nl4m5.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"akshay",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)
