import pymongo


class Session:
    __client = pymongo.MongoClient("mongodb://localhost:27017/")

    @staticmethod
    def get_client():
        return Session.__client
