import pytest
import jwt
from datetime import datetime

from ..provider import CompProvider
from ..schemas import Competition


def test_add_comp():
    comp_prov = CompProvider()
    competition_id = 123
    allowed_styles = []
    entries_close_date = datetime.now()
    awards_date = datetime.now()
    description = "blah blah blah"
    comp_prov.create_comp(
        Competition(
            competition_id=competition_id,
            allowed_styles=allowed_styles,
            entries_close_date=entries_close_date,
            awards_date=awards_date,
            description=description,
        )
    )
    assert comp_prov.get_comp(competition_id).competition_id == competition_id


def test_add_remove_comp():
    comp_prov = CompProvider()
    competition_id = 123
    allowed_styles = []
    entries_close_date = datetime.now()
    awards_date = datetime.now()
    description = "blah blah blah"
    comp_prov.create_comp(
        Competition(
            competition_id=competition_id,
            allowed_styles=allowed_styles,
            entries_close_date=entries_close_date,
            awards_date=awards_date,
            description=description,
        )
    )
    comp_prov.remove_comp(competition_id=competition_id)
    assert not comp_prov.get_comp(competition_id)


def test_update_comp_allowed_styles():
    comp_prov = CompProvider()
    competition_id = 123
    allowed_styles = []
    entries_close_date = datetime.now()
    awards_date = datetime.now()
    description = "blah blah blah"
    comp_prov.create_comp(
        Competition(
            competition_id=competition_id,
            allowed_styles=allowed_styles,
            entries_close_date=entries_close_date,
            awards_date=awards_date,
            description=description,
        )
    )
    stored_comp = comp_prov.get_comp(competition_id)
    new_allowed_styles = 321
    stored_comp.allowed_styles = new_allowed_styles
    comp_prov.update_comp(stored_comp)
    assert comp_prov.get_comp(competition_id).allowed_styles == new_allowed_styles


def test_update_comp_entries_close_date():
    comp_prov = CompProvider()
    competition_id = 123
    allowed_styles = []
    entries_close_date = datetime.now()
    awards_date = datetime.now()
    description = "blah blah blah"
    comp_prov.create_comp(
        Competition(
            competition_id=competition_id,
            allowed_styles=allowed_styles,
            entries_close_date=entries_close_date,
            awards_date=awards_date,
            description=description,
        )
    )
    stored_comp = comp_prov.get_comp(competition_id)
    new_entries_close_date = datetime.now()
    stored_comp.entries_close_date = new_entries_close_date
    comp_prov.update_comp(stored_comp)
    assert (
        comp_prov.get_comp(competition_id).entries_close_date == new_entries_close_date
    )


def test_update_comp_awards_date():
    comp_prov = CompProvider()
    competition_id = 123
    allowed_styles = []
    entries_close_date = datetime.now()
    awards_date = datetime.now()
    description = "blah blah blah"
    comp_prov.create_comp(
        Competition(
            competition_id=competition_id,
            allowed_styles=allowed_styles,
            entries_close_date=entries_close_date,
            awards_date=awards_date,
            description=description,
        )
    )
    stored_comp = comp_prov.get_comp(competition_id)
    new_awards_date = datetime.now()
    stored_comp.awards_date = new_awards_date
    comp_prov.update_comp(stored_comp)
    assert comp_prov.get_comp(competition_id).awards_date == new_awards_date


def test_update_comp_description():
    comp_prov = CompProvider()
    competition_id = 123
    allowed_styles = []
    entries_close_date = datetime.now()
    awards_date = datetime.now()
    description = "blah blah blah"
    comp_prov.create_comp(
        Competition(
            competition_id=competition_id,
            allowed_styles=allowed_styles,
            entries_close_date=entries_close_date,
            awards_date=awards_date,
            description=description,
        )
    )
    stored_comp = comp_prov.get_comp(competition_id)
    new_description = "a new description"
    stored_comp.description = new_description
    comp_prov.update_comp(stored_comp)
    assert comp_prov.get_comp(competition_id).description == new_description
