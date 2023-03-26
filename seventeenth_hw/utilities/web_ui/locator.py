class Locator:
    def __init__(self, method: str, locator: str):
        self.__method = method
        self.__locator = locator

    def get_locator(self) -> tuple:
        return self.__method, self.__locator
