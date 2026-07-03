from pymongo import MongoClient 

uri = "mongodb+srv://abhiaitech:Admin123@cluster0.ssimn0v.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)