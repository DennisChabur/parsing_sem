from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client['books'] # выбор бзд

collection = db['books_data']

with open('books_data.json', 'r') as file:
    data = json.load(file)
for book in data:
    collection.insert_one(book)


# каунтер
all_books = collection.count_documents({})
print(f'whole amount = {all_books}')

count_books = collection.count_documents(filter={'stock': {'$lt': 20}})
print(f"number of books in stock less then 20 = {count_books}")

query = filter={'price': {'$gte': 20.00}}
print(f"num of books with price more than 20$:{collection.count_documents(query)}")

query = filter={'book_name': {'$regex': '^[AT]'}}
projection = {'book_name': 1, '_id': 0}
project_docs = collection.find(query, projection)

for doc in project_docs:
    print(doc)