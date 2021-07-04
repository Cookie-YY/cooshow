from flask import g, request


def authentication(request_args):
    from app import app
    LOGIN_AUTH = app.config.get("LOGIN_AUTH", False)
    LEVEL_AUTH = app.config.get("LEVEL_AUTH", False)
    LEVEL_AUTH_PARAM = app.config.get("LEVEL_AUTH_PARAM")
    LEVEL_AUTH_COOKIE = app.config.get("LEVEL_AUTH_COOKIE")
    LEVEL_AUTH_ENCRYPT = app.config.get("LEVEL_AUTH_ENCRYPT")
    if LOGIN_AUTH:
        pass
    if LEVEL_AUTH and not g.get("level_auth", ""):
        if LEVEL_AUTH_PARAM:
            g.level_auth = request_args.get(LEVEL_AUTH_PARAM, "")
        if not g.level_auth and LEVEL_AUTH_COOKIE:
            g.level_auth = request.cookies.get(LEVEL_AUTH_COOKIE, "")

    return 200, "success", {}