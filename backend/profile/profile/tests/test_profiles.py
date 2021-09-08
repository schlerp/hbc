from ..schemas import UserProfile
from ..provider import ProfileProvider


def test_add_profile():
    profile_prov = ProfileProvider()
    username = "imauser"
    first_name = "john"
    last_name = "smith"
    bio = "Bleep blerp, herp derp."
    avatar = b"someimagebinary"
    profile_prov.create_profile(
        UserProfile(
            username=username,
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            avatar=avatar,
        )
    )


def test_add_remove_profile():
    profile_prov = ProfileProvider()
    username = "imauser"
    first_name = "john"
    last_name = "smith"
    bio = "Bleep blerp, herp derp."
    avatar = b"someimagebinary"
    profile_prov.create_profile(
        UserProfile(
            username=username,
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            avatar=avatar,
        )
    )
    profile_prov.remove_profile(username)


def test_update_first_name_profile():
    profile_prov = ProfileProvider()
    username = "imauser"
    first_name = "john"
    last_name = "smith"
    bio = "Bleep blerp, herp derp."
    avatar = b"someimagebinary"
    profile_prov.create_profile(
        UserProfile(
            username=username,
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            avatar=avatar,
        )
    )
    new_first_name = "johnny"
    stored_profile = profile_prov.get_profile(username)
    stored_profile.first_name = new_first_name
    profile_prov.update_profile(stored_profile)
    assert profile_prov.get_profile(username).first_name == new_first_name


def test_update_last_name_profile():
    profile_prov = ProfileProvider()
    username = "imauser"
    first_name = "john"
    last_name = "smith"
    bio = "Bleep blerp, herp derp."
    avatar = b"someimagebinary"
    profile_prov.create_profile(
        UserProfile(
            username=username,
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            avatar=avatar,
        )
    )
    new_last_name = "smithy"
    stored_profile = profile_prov.get_profile(username)
    stored_profile.last_name = new_last_name
    profile_prov.update_profile(stored_profile)
    assert profile_prov.get_profile(username).last_name == new_last_name


def test_update_bio_profile():
    profile_prov = ProfileProvider()
    username = "imauser"
    first_name = "john"
    last_name = "smith"
    bio = "Bleep blerp, herp derp."
    avatar = b"someimagebinary"
    profile_prov.create_profile(
        UserProfile(
            username=username,
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            avatar=avatar,
        )
    )
    new_bio = "i am the new bio"
    stored_profile = profile_prov.get_profile(username)
    stored_profile.bio = new_bio
    profile_prov.update_profile(stored_profile)
    assert profile_prov.get_profile(username).bio == new_bio


def test_update_avatar_profile():
    profile_prov = ProfileProvider()
    username = "imauser"
    first_name = "john"
    last_name = "smith"
    bio = "Bleep blerp, herp derp."
    avatar = b"someimagebinary"
    profile_prov.create_profile(
        UserProfile(
            username=username,
            first_name=first_name,
            last_name=last_name,
            bio=bio,
            avatar=avatar,
        )
    )
    new_avatar = b"somenewimagebinary"
    stored_profile = profile_prov.get_profile(username)
    stored_profile.avatar = new_avatar
    profile_prov.update_profile(stored_profile)
    assert profile_prov.get_profile(username).avatar == new_avatar
