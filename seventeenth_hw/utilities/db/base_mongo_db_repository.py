class BaseMongoDbRepository:
    def __init__(self, collection):
        self.collection = collection

    def _find_one(self, input_data):
        return self.collection.find_one(input_data)

    def _find_by(self, input_data):
        find = self.collection.find(input_data)
        for result in find:
            return result

    def _insert_one(self, input_data):
        self.collection.insert_one(input_data)

    def _insert_many(self, input_data):
        self.collection.insert_many(input_data)

    def _delete_one(self, input_data):
        self.collection.delete_one(input_data)

    def _delete_many(self, input_data):
        self.collection.delete_many(input_data)

    def _add_or_update_many(self, query, input_data):
        self.collection.update_many(query, input_data)

    def _unset_many(self, query, input_data):
        self.collection.update_many(query, input_data)
