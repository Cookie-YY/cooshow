def get_error_msg(code):
    error_code2msg = {
        400: "NoSuchTableError: ater trying all of the candidate tables, nothing found"
    }

    return error_code2msg.get(code, "Undefined error")