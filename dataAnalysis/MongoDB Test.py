# Example 11.20
# pip install pymongo
# pip install dnspython
import pymongo
from pymongo import MongoClient

# Replace the content inside MongoClient("...") with your own generated code
# Replace <username> and <password> with your own username and password
cluster = MongoClient("mongodb+srv://<username>:<password>@cluster0.6alke.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster.test
collection = db['test']

post1 = {"_id": 0, "name": "Tom", "mark": 54}
post2 = {"_id": 1, "name": "John", "mark": 78}
#collection.insert_one(post1)
collection.insert_many([post1,post2])

#results = collection.find()
results = collection.find({"name":"John"})
for result in results:
    print(result)
