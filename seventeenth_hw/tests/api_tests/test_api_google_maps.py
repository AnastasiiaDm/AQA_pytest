import re

from http import HTTPStatus

import pytest

from seventeenth_hw.api_collections.find_place_api import FindPlaceAPI
from seventeenth_hw.data_objecs.place_data import PlaceData


@pytest.mark.regressoin
def test_get_place_api_status_request_denied(env, place_mock):
    expected_place = place_mock
    response = FindPlaceAPI(env).get_place('json')
    response_data = response.json()
    actual_place = PlaceData.from_json(**response_data)
    assert response.status_code == HTTPStatus.OK, f"Response status code is not 200, " \
                                                  f"actual status code is {response.status_code}"
    assert actual_place == expected_place, f'Place data is not "{expected_place}", actual data is "{actual_place}"'


@pytest.mark.smoke
@pytest.xfail
def test_get_place_api_status_ok(env):
    response = FindPlaceAPI(env).get_place('json')
    response_status = re.search('"status"\s:\s"(.*)"', response.text)
    error_message = re.search('"error_message"\s:\s"(.*)"', response.text)
    assert response_status.group(1) == "OK", f"Search status is not 'OK', actual status is " \
                                             f"'{response_status.group(1)}' error message is: \n{error_message.group(1)}"
