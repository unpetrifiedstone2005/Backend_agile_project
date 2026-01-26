import pytest
from src.database.models import UserProfile
from src.services.profileSkillService import ProfileDraftSkillService
from src.tests.unit.fakes import FakeSkillRepository

@pytest.fixture
def skill_repo():
    # fixed skills in DB
    return FakeSkillRepository({1:"DBMS",2:"Python",3:"Cloud"})


@pytest.fixture
def skill_service(skill_repo):
    return ProfileDraftSkillService(skill_repo)


@pytest.fixture
def draft():
    return UserProfile(
        user_name="riddhi",
        name="Riddhi Sinha",
    )


# ----------------------------
# Unit Tests
# ----------------------------

def test_add_skill_success(skill_service, draft):
    skill_service.add_skill(draft, skill_id=1)

    assert draft.skills == [1]


def test_add_invalid_skill(skill_service, draft):
    with pytest.raises(ValueError, match="Invalid skill ID"):
        skill_service.add_skill(draft, skill_id=99)


def test_add_duplicate_skill(skill_service, draft):
    skill_service.add_skill(draft, skill_id=1)

    with pytest.raises(ValueError, match="already added"):
        skill_service.add_skill(draft, skill_id=1)


def test_remove_skill_success(skill_service, draft):
    skill_service.add_skill(draft, skill_id=1)

    skill_service.remove_skill(draft, skill_id=1)

    assert draft.skills == []


def test_remove_skill_not_present(skill_service, draft):
    with pytest.raises(ValueError, match="not present"):
        skill_service.remove_skill(draft, skill_id=1)