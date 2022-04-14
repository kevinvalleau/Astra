import os

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


# Mongo DB connection
def db_connect():
    maxSevSelDelay = 3000
    try:
        mongo_host = 'localhost'
        mongo_port = 27018

        if 'MONGO_PORT_27017_TCP_ADDR' in os.environ :
            mongo_host = os.environ['MONGO_PORT_27017_TCP_ADDR']

        if 'MONGO_PORT_27017_TCP_PORT' in os.environ:
            mongo_port = int(os.environ['MONGO_PORT_27017_TCP_PORT'])

        client = MongoClient(mongo_host, mongo_port, serverSelectionTimeoutMS=maxSevSelDelay)
        client.server_info()
        return client

    except ServerSelectionTimeoutError as err:
        exit("db_connect - Failed to connect to MongoDB.")