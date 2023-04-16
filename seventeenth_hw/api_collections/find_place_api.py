from seventeenth_hw.data_objecs.place_data import PlaceData
from seventeenth_hw.utilities.api.base_api import BaseAPI
from seventeenth_hw.utilities.web_ui.decorators import allure_step


@allure_step
class FindPlaceAPI(BaseAPI):
    def __init__(self, env):
        super().__init__(env)
        self.__place_api = '/place/findplacefromtext'

    def get_place(self, data_type, headers=None):
        """
        :param data_type: 'json' or 'xml'
        """
        return self._get(url=f'{self.__place_api}/{data_type}', headers=headers)

    def create_place(self, body=PlaceData(), headers=None, **kwargs):
        body.update_data(**kwargs)
        return self._post(f'{self.__place_api}/', body=body.get_json(), headers=headers)
