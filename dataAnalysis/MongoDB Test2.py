# Example 11.21
# pip install pymongo
# pip install dnspython
import pymongo
from pymongo import MongoClient

# Replace the content inside MongoClient("...") with your own generated code
# Replace <username> and <password> with your own username and password
cluster = MongoClient("mongodb+srv://<username>:<password>@cluster0.6alke.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster.test
collection = db['test']

#Save image to MongoDB
import gridfs

#Create an object of GridFs for the above database.
fs = gridfs.GridFS(db)

#define an image object with the location.
file = "child.jpg"

#Open the image in read-only format.
with open(file, 'rb') as f:
    contents = f.read()

#Now store/put the image via GridFs object.
fs.put(contents, filename="file")
