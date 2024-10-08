from pymongo import MongoClient
from datetime import datetime

# Подключение к MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['foo']
collection = db['bar']

document = {
    'data': 'Пример данных',
    'createdAt': datetime.now(),
}

# Вставка документа в коллекцию
collection.insert_one(document)

day = 24 * 3600  # 1 день в секундах

# Создание TTL индекса на поле createdAt
# https://pymongo.readthedocs.io/en/stable/api/pymongo/collection.html#pymongo.collection.Collection.create_index
db.collection.createIndex({"createdAt": 1}, expireAfterSeconds=day)
