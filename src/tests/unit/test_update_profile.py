import pytest
from src.database.models import UserProfile
from src.services.profileUpdate import ProfileUpdateService
from src.tests.unit.fakes import FakeProfileRepository, FakeSkillRepository, FakeRoleRepository

@pytest.fixture
def existing_profile():
    return UserProfile(
        user_name="riddhi",
        name="Riddhi Sinha",
        skills=[1, 2],
        roles=[1],
    )


@pytest.fixture
def profile_repo(existing_profile):
    return FakeProfileRepository(
        profile={"riddhi": existing_profile}
    )


@pytest.fixture
def skill_repo():
    return FakeSkillRepository({
        1: "Python",
        2: "DBMS",
        3: "Cloud",
    })


@pytest.fixture
def role_repo():
    return FakeRoleRepository({
        1: "Developer",
        2: "Admin",
    })


@pytest.fixture
def update_service(profile_repo, skill_repo, role_repo):
    return ProfileUpdateService(
        profile_repo=profile_repo,
        skill_repo=skill_repo,
        role_repo=role_repo,
    )


# ----------------------------
# Unit Tests
# ----------------------------

def test_update_name_success(update_service, profile_repo):
    profile = update_service.update_profile(
        user_name="riddhi",
        name="New Name",
        skills=None,
        roles=None,
    )

    assert profile.name == "New Name"
    assert profile_repo.saved_profile is profile


def test_update_skills_success(update_service):
    profile = update_service.update_profile(
        user_name="riddhi",
        name=None,
        skills=[1, 3],
        roles=None,
    )

    assert set(profile.skills) == {1, 3}


def test_update_roles_success(update_service):
    profile = update_service.update_profile(
        user_name="riddhi",
        name=None,
        skills=None,
        roles=[2],
    )

    assert profile.roles == [2]


def test_update_all_fields_success(update_service):
    profile = update_service.update_profile(
        user_name="riddhi",
        name="Updated Name",
        skills=[2, 3],
        roles=[1, 2],
    )

    assert profile.name == "Updated Name"
    assert set(profile.skills) == {2, 3}
    assert set(profile.roles) == {1, 2}


def test_profile_not_found(update_service):
    with pytest.raises(ValueError, match="Profile not found"):
        update_service.update_profile(
            user_name="unknown",
            name="Name",
            skills=[1],
            roles=[1],
        )


def test_invalid_skill_id(update_service):
    with pytest.raises(ValueError, match="Invalid skill ID"):
        update_service.update_profile(
            user_name="riddhi",
            name=None,
            skills=[99],
            roles=None,
        )


def test_invalid_role_id(update_service):
    with pytest.raises(ValueError, match="Invalid role ID"):
        update_service.update_profile(
            user_name="riddhi",
            name=None,
            skills=None,
            roles=[99],
        )


def test_empty_name_not_allowed(update_service):
    with pytest.raises(ValueError, match="Name cannot be empty"):
        update_service.update_profile(
            user_name="riddhi",
            name="",
            skills=None,
            roles=None,
        )