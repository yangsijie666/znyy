class Error:
    code: str
    message: str

    def __init__(self, code: str, message: str):
        self.code = code
        self.message = message


def build_error(err_code: str, err_msg: str):
    return Error(err_code, err_msg)


def params_missing(err_msg: str):
    return Error("PARAMETER_MISSING", err_msg)


def not_found(err_msg: str):
    return Error("NOT_FOUND", err_msg)
