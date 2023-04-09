import pytest

from seventeenth_hw.data_objecs.place_data import PlaceData


@pytest.fixture()
def place_mock():
    return PlaceData()
