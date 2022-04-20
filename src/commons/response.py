class AppResponse:
    def __init__(self, code, status, message):
        self.code = code
        self.status = status
        self.message = message

    def to_json(self):
        return self.__dict__