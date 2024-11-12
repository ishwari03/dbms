from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["my_database"]  # replace with your database name
collection = db["my_collection"]  # replace with your collection name

# Create (Insert) a document
def add_document(data):
    result = collection.insert_one(data)
    print(f"Document inserted with ID: {result.inserted_id}")

# Read (Find) documents
def get_documents():
    documents = collection.find()
    for doc in documents:
        print(doc)

# Update a document
def update_document(query, new_values):
    result = collection.update_one(query, {"$set": new_values})
    print(f"Documents updated: {result.modified_count}")

# Delete a document
def delete_document(query):
    result = collection.delete_one(query)
    print(f"Documents deleted: {result.deleted_count}")

# Sample usage
add_document({"name": "Alice", "age": 25})
get_documents()
update_document({"name": "Alice"}, {"age": 26})
delete_document({"name": "Alice"})