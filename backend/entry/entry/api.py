import os
from typing import List
from fastapi import FastAPI, Depends

from .provider import EntryProvider
from .schemas import CompetitionEntry
from .exceptions import (
    to_http_exception,
    exist_exc_resp,
    no_exist_exc_resp,
    generic_exc_resp,
)

description = "The entry microservice provides functionality and storage related to competition entries."

tags_metadata = [{"name": "CRUD", "description": "CRUD operations for entries"}]

app = FastAPI(
    title="HBC: Entry uService",
    description=description,
    version="0.0.1",
    openapi_tags=tags_metadata,
)

provider = EntryProvider()


async def get_prov():
    return provider


@app.get(
    "/entry",
    status_code=200,
    response_model=List[CompetitionEntry],
    responses={**no_exist_exc_resp, **generic_exc_resp},
    tags=["CRUD"],
)
async def get_entry(_prov: EntryProvider = Depends(get_prov)):
    try:
        return _prov.get_all()
    except Exception as e:
        raise to_http_exception(e)


@app.get(
    "/entry/{entry_id}",
    status_code=200,
    response_model=CompetitionEntry,
    responses={**no_exist_exc_resp, **generic_exc_resp},
    tags=["CRUD"],
)
async def get_entry(entry_id: int, _prov: EntryProvider = Depends(get_prov)):
    try:
        return _prov.get_entry(entry_id)
    except Exception as e:
        raise to_http_exception(e)


@app.post(
    "/entry",
    status_code=201,
    response_description="Entry created",
    responses=exist_exc_resp,
    tags=["CRUD"],
)
async def create_entry(
    entry: CompetitionEntry, _prov: EntryProvider = Depends(get_prov)
):
    try:
        _prov.create_entry(entry)
    except Exception as e:
        raise to_http_exception(e)


@app.put(
    "/entry/{entry_id}",
    status_code=204,
    response_description="Entry updated",
    responses=no_exist_exc_resp,
    tags=["CRUD"],
)
async def update_entry(
    entry_id: str, entry: CompetitionEntry, _prov: EntryProvider = Depends(get_prov)
):
    try:
        status = _prov.update_entry(entry)
    except Exception as e:
        raise to_http_exception(e)


@app.delete(
    "/entry/{entry_id}",
    status_code=204,
    response_description="Entry deleted",
    responses=no_exist_exc_resp,
    tags=["CRUD"],
)
async def remove_entry(entry_id: int, _prov: EntryProvider = Depends(get_prov)):
    try:
        status = _prov.remove_entry(entry_id)
    except Exception as e:
        raise to_http_exception(e)
