import pymongo
from common import mongo_config as config
from util import mongo_url


class MongoDB(object):
    __host = None

    def __init__(self, collection=None):

        self.__collection = collection
        self.__client = pymongo.MongoClient(mongo_url)

    def get_database(self, database=None):
        """
        :param database: 库名
        :return:  pymongo.database.Database
        """
        if not database:
            database = db = config['database']
        return self.__client[database]

    def get_collection(self, collection=None, database=None):
        """
        :param collection: 表名
        :param database: 库名
        :return: pymongo.collection.Collection
        """
        if not collection:
            assert self.__collection is not None, '参数 collection 不合法'
            collection = self.__collection
        return self.get_database(database)[collection]

    def __enter__(self):
        return self.get_database()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__client.close()


class MongoCollection(MongoDB):

    def __enter__(self):
        return self.get_collection()


def mongo_db(collection=None):
    return MongoDB(collection)


def mongo_collection(collection=None):
    return MongoCollection(collection)
