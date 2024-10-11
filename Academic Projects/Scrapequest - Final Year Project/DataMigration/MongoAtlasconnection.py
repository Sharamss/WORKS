from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def test_mongodb_connection(uri):
    """Attempt to connect to MongoDB Atlas using the provided URI."""
    try:
        # Connect to the MongoDB client
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)  # 5 second timeout
        # Attempt to fetch a small amount of data
        client.admin.command('ping')
        print("MongoDB connection successful.")
    except ConnectionFailure as e:
        print(f"MongoDB connection failed: {e}")

# 'uri' = MongoDB Atlas connection string
uri = "mongodb+srv://sharams:Su9860797972@atlascluster.abktl4t.mongodb.net/"
test_mongodb_connection(uri)