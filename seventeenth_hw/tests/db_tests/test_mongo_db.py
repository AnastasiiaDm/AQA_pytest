from seventeenth_hw.utilities.db.base_mongo_db_repository import BaseMongoDbRepository


def test_insert_one_and_delete_one(get_alternate_signs_col, env):
    alternate_col = get_alternate_signs_col
    BaseMongoDbRepository(alternate_col)._insert_one(env.face_dict)
    print('------------------')
    BaseMongoDbRepository(alternate_col)._find_by(env.face_dict)
    print('------------------')
    BaseMongoDbRepository(alternate_col)._find_by({})
    print('------------------')
    BaseMongoDbRepository(alternate_col)._insert_many(env.face_list_of_dicts)
    BaseMongoDbRepository(alternate_col)._find_by({})
    print('------------------')
    BaseMongoDbRepository(alternate_col)._delete_one(env.face_dict)
    BaseMongoDbRepository(alternate_col)._find_by({})
    print('------------------')
    # can't use env for delete_many cause this step has been skipped without fail and without deleting
    BaseMongoDbRepository(alternate_col)._delete_many({"face_key": "face_value"})
    BaseMongoDbRepository(alternate_col)._find_by({})
    print('------------------')
    BaseMongoDbRepository(alternate_col)._add_or_update_many({}, env.sta_cost_update)
    BaseMongoDbRepository(alternate_col)._find_by({})
    print('------------------')
    BaseMongoDbRepository(alternate_col)._unset_many({}, env.sta_cost_unset)
    BaseMongoDbRepository(alternate_col)._find_by({})
    print('------------------')
    BaseMongoDbRepository(alternate_col)._find_one(env.sign_name)
