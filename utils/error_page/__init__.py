class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message or InvalidUsage.get_msg(self.status_code)
        return rv

    @staticmethod
    def get_msg(code):
        code_dict = {
            400: f" NoSuchTableError: ater trying all of the candidate tables, nothing found"
        }
        return code_dict.get(code, "Undefined error")