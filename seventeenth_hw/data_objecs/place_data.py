class PlaceData:
    def __init__(self, **kwargs):
        self.candidates = [] if "candidates" not in kwargs.keys() else kwargs['candidates']
        self.error_message = "You must use an API key to authenticate each request to Google Maps Platform APIs. " \
                             "For additional information, please refer to http://g.co/dev/maps-no-account" \
                             "" if 'error_message' not in kwargs.keys() else kwargs['error_message']
        self.request_denied = 'REQUEST_DENIED' if 'request_denied' not in kwargs.keys() else kwargs['request_denied']

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
