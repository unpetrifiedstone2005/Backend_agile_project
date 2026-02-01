import pytest
from src.database.models import UserProfile
from src.services.profileRoleService import ProfileDraftRoleService
from src.tests.unit.fakes import FakeRoleRepository

@pytest.fixture
def role_repo():
    # fixed roles in DB
    return FakeRoleRepository({1:"Tester", 2:"DevOps", 3:"Developer"})


@pytest.fixture
def role_service(role_repo):
    return ProfileDraftRoleService(role_repo)


@pytest.fixture
def draft():
    return UserProfile(
        user_name="riddhi",
        name="Riddhi Sinha",
    )


# ----------------------------
# Unit Tests
# ----------------------------

def test_add_role_success(role_service, draft):
    role_service.add_role(draft, role_id=1)

    assert draft.roles == [1]

def test_add_invalid_role(role_service, draft):
    with pytest.raises(ValueError, match="Invalid role ID"):
        role_service.add_role(draft, role_id=99)


def test_add_duplicate_role(role_service, draft):
    role_service.add_role(draft, role_id=1)

    with pytest.raises(ValueError, match="already added"):
        role_service.add_role(draft, role_id=1)


def test_remove_role_success(role_service, draft):
    role_service.add_role(draft, role_id=1)

    role_service.remove_role(draft, role_id=1)

    assert draft.roles == []


def test_remove_role_not_present(role_service, draft):
    with pytest.raises(ValueError, match="not present"):
        role_service.remove_role(draft, role_id=1)