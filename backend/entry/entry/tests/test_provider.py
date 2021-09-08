import pytest
import jwt

from ..provider import EntryProvider
from ..schemas import CompetitionEntry


def test_add_entry():
    entry_prov = EntryProvider()
    username = "test_add_user"
    competition_id = 123
    entry_id = 123
    name = "derp"
    category = "12"
    subcategory = "c"
    notes = "some important notes."
    entry_prov.create_entry(
        CompetitionEntry(
            username=username,
            competition_id=competition_id,
            entry_id=entry_id,
            name=name,
            category=category,
            subcategory=subcategory,
            notes=notes,
        )
    )
    assert entry_prov.get_entry(entry_id).entry_id == entry_id


def test_add_remove_entry():
    entry_prov = EntryProvider()
    username = "test_add_user"
    competition_id = 123
    entry_id = 123
    name = "derp"
    category = "12"
    subcategory = "c"
    notes = "some important notes."
    entry_prov.create_entry(
        CompetitionEntry(
            username=username,
            competition_id=competition_id,
            entry_id=entry_id,
            name=name,
            category=category,
            subcategory=subcategory,
            notes=notes,
        )
    )
    entry_prov.remove_entry(entry_id=entry_id)
    assert not entry_prov.get_entry(entry_id)


def test_update_entry_username():
    entry_prov = EntryProvider()
    username = "test_add_user"
    competition_id = 123
    entry_id = 123
    name = "derp"
    category = "12"
    subcategory = "c"
    notes = "some important notes."
    entry_prov.create_entry(
        CompetitionEntry(
            username=username,
            competition_id=competition_id,
            entry_id=entry_id,
            name=name,
            category=category,
            subcategory=subcategory,
            notes=notes,
        )
    )
    stored_entry = entry_prov.get_entry(entry_id)
    new_username = "test321"
    stored_entry.username = new_username
    entry_prov.update_entry(stored_entry)
    assert entry_prov.get_entry(entry_id).username == new_username


def test_update_entry_name():
    entry_prov = EntryProvider()
    username = "test_add_user"
    competition_id = 123
    entry_id = 123
    name = "derp"
    category = "12"
    subcategory = "c"
    notes = "some important notes."
    entry_prov.create_entry(
        CompetitionEntry(
            username=username,
            competition_id=competition_id,
            entry_id=entry_id,
            name=name,
            category=category,
            subcategory=subcategory,
            notes=notes,
        )
    )
    stored_entry = entry_prov.get_entry(entry_id)
    new_name = "test321"
    stored_entry.name = new_name
    entry_prov.update_entry(stored_entry)
    assert entry_prov.get_entry(entry_id).name == new_name


def test_update_entry_category():
    entry_prov = EntryProvider()
    username = "test_add_user"
    competition_id = 123
    entry_id = 123
    name = "derp"
    category = "12"
    subcategory = "c"
    notes = "some important notes."
    entry_prov.create_entry(
        CompetitionEntry(
            username=username,
            competition_id=competition_id,
            entry_id=entry_id,
            name=name,
            category=category,
            subcategory=subcategory,
            notes=notes,
        )
    )
    stored_entry = entry_prov.get_entry(entry_id)
    new_category = "test321"
    stored_entry.category = new_category
    entry_prov.update_entry(stored_entry)
    assert entry_prov.get_entry(entry_id).category == new_category


def test_update_entry_subcategory():
    entry_prov = EntryProvider()
    username = "test_add_user"
    competition_id = 123
    entry_id = 123
    name = "derp"
    category = "12"
    subcategory = "c"
    notes = "some important notes."
    entry_prov.create_entry(
        CompetitionEntry(
            username=username,
            competition_id=competition_id,
            entry_id=entry_id,
            name=name,
            category=category,
            subcategory=subcategory,
            notes=notes,
        )
    )
    stored_entry = entry_prov.get_entry(entry_id)
    new_subcategory = "test321"
    stored_entry.subcategory = new_subcategory
    entry_prov.update_entry(stored_entry)
    assert entry_prov.get_entry(entry_id).subcategory == new_subcategory


def test_update_entry_notes():
    entry_prov = EntryProvider()
    username = "test_add_user"
    competition_id = 123
    entry_id = 123
    name = "derp"
    category = "12"
    subcategory = "c"
    notes = "some important notes."
    entry_prov.create_entry(
        CompetitionEntry(
            username=username,
            competition_id=competition_id,
            entry_id=entry_id,
            name=name,
            category=category,
            subcategory=subcategory,
            notes=notes,
        )
    )
    stored_entry = entry_prov.get_entry(entry_id)
    new_notes = "test321"
    stored_entry.notes = new_notes
    entry_prov.update_entry(stored_entry)
    assert entry_prov.get_entry(entry_id).notes == new_notes
