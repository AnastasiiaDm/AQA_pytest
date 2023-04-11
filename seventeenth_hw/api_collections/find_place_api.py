from seventeenth_hw.utilities.api.base_api import BaseAPI


class FindPlaceAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__place_api = '/place/findplacefromtext'

    def get_place(self, data_type, headers=None):
        """
        :param data_type: 'json' or 'xml'
        """
        return self._get(url=f'{self.__place_api}/{data_type}', headers=headers)
