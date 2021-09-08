from fastapi import HTTPException


class EntryExistsException(Exception):
    pass


class NoMatchingEntryException(Exception):
    pass


exist_exc = HTTPException(403, "Entry exists")
exist_exc_resp = {exist_exc.status_code: {"description": exist_exc.detail}}

no_exist_exc = HTTPException(404, "Entry not found")
no_exist_exc_resp = {no_exist_exc.status_code: {"description": no_exist_exc.detail}}

generic_exc = HTTPException(500, "An internal exception occurred")
generic_exc_resp = {generic_exc.status_code: {"description": generic_exc.detail}}


def to_http_exception(exc: Exception) -> HTTPException:
    if type(exc) == EntryExistsException:
        return exist_exc
    elif type(exc) == NoMatchingEntryException:
        return no_exist_exc
    return generic_exc
