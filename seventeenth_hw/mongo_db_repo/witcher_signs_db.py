from mongo_db_session import Session


class WitcherSigns(Session):
    __signs_db = Session.get_client()["witcher_signs"]

    @staticmethod
    def get_signs_db():
        return WitcherSigns.__signs_db
