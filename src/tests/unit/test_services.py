import pytest
from src.database.models import UserProfile
from src.tests.unit.fakes import FakeProfileRepository, FakeSkillRepository, FakeRoleRepository

from src.services.profileCreate import ProfileCreationService


# =========================
# Fixtures
# =========================

@pytest.fixture
def profile_repo():
    return FakeProfileRepository()


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
def creation_service(profile_repo, skill_repo, role_repo):
    return ProfileCreationService(
        profile_repo=profile_repo,
        skill_repo=skill_repo,
        role_repo=role_repo,
    )


# =========================
# Unit Tests
# =========================

def test_create_profile_success(creation_service, profile_repo):
    profile = creation_service.create_profile(
        user_name="riddhi",
        name="Riddhi Sinha",
        skills=[1, 2],
        roles=[1],
    )

    assert profile.user_name == "riddhi"
    assert profile.name == "Riddhi Sinha"
    assert set(profile.skills) == {1, 2}
    assert profile.roles == [1]
    assert profile_repo.exists("riddhi")


def test_duplicate_user_not_allowed(creation_service):
    creation_service.create_profile(
        user_name="riddhi",
        name="Riddhi Sinha",
        skills=[1],
        roles=[1],
    )

    with pytest.raises(ValueError, match="User already exists"):
        creation_service.create_profile(
            user_name="riddhi",
            name="Another Name",
            skills=[2],
            roles=[1],
        )


def test_empty_username_not_allowed(creation_service):
    with pytest.raises(ValueError, match="Username is required"):
        creation_service.create_profile(
            user_name="",
            name="Name",
            skills=[1],
            roles=[1],
        )


def test_empty_name_not_allowed(creation_service):
    with pytest.raises(ValueError, match="Name is required"):
        creation_service.create_profile(
            user_name="riddhi",
            name="",
            skills=[1],
            roles=[1],
        )


def test_no_skills_not_allowed(creation_service):
    with pytest.raises(ValueError, match="At least one skill is required"):
        creation_service.create_profile(
            user_name="riddhi",
            name="Name",
            skills=[],
            roles=[1],
        )


def test_no_roles_not_allowed(creation_service):
    with pytest.raises(ValueError, match="At least one role is required"):
        creation_service.create_profile(
            user_name="riddhi",
            name="Name",
            skills=[1],
            roles=[],
        )


def test_invalid_skill_id_not_allowed(creation_service):
    with pytest.raises(ValueError, match="Invalid skill ID"):
        creation_service.create_profile(
            user_name="riddhi",
            name="Name",
            skills=[99],
            roles=[1],
        )


def test_invalid_role_id_not_allowed(creation_service):
    with pytest.raises(ValueError, match="Invalid role ID"):
        creation_service.create_profile(
            user_name="riddhi",
            name="Name",
            skills=[1],
            roles=[99],
        )


