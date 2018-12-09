#!/usr/bin/env python3


import pymongo
import redis
import logging
from config import Config

class Log():
    def get_logger():
        logger = logging.getLogger(__name__)
        logger.setLevel(level = logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


        handler = logging.FileHandler(Config.log_app_path)
        handler.setFormatter(formatter)

        console = logging.StreamHandler()
        console.setFormatter(formatter)

        logger.addHandler(handler)
        logger.addHandler(console)

        return logger

class Redis():
    def get_redis(self):
        redis_pool= redis.ConnectionPool(host=Config.redis_host,port=Config.redis_port,decode_responses=True)


class MongoDB():
    def __init__(self):
        mongo_client = pymongo.MongoClient(Config.mongo_host, Config.mongo_port)
        self.db = mongo_client.get_database(Config.mongo_db)
        self.db.authenticate(Config.mongo_user, Config.mongo_pwd)

    def get_collection(self, collection):
        self.collection = eval("self.db." + collection)
        return self.collection
