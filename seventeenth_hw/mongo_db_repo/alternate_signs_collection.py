from seventeenth_hw.mongo_db_repo.witcher_signs_db import WitcherSigns


class AlternateSigns(WitcherSigns):
    __alternate_signs_col = WitcherSigns.get_signs_db()["alternate_signs"]

    @staticmethod
    def get_col():
        return AlternateSigns.__alternate_signs_col
