import os
from fastapi import FastAPI, Depends

from .provider import CompProvider
from .schemas import Competition

app = FastAPI(
    title="HBC: Comp uService",
    description="Provides functionality and data related to competitions",
    version="0.0.1",
)
provider = CompProvider()


async def get_prov():
    return provider


@app.get("/comp")
async def get_all_comps(_prov: CompProvider = Depends(get_prov)):
    return _prov.get_all_comps()


@app.get("/comp/{competitionId}")
async def get_comp(competitionId: str, _prov: CompProvider = Depends(get_prov)):
    return _prov.get_comp(competitionId)


@app.post("/comp")
async def create_comp(comp: Competition, _prov: CompProvider = Depends(get_prov)):
    return _prov.create_comp(comp)


@app.put("/comp")
async def update_comp(comp: Competition, _prov: CompProvider = Depends(get_prov)):
    return _prov.update_comp(comp)


@app.delete("/comp/{competitionId}")
async def remove_comp(competitionId: str, _prov: CompProvider = Depends(get_prov)):
    return _prov.remove_comp(competitionId)
