from src.database_2.db import SessionLocal
from src.database_2.models import (
    Student, Skill, Role, StudentSkill, StudentRole
)

db = SessionLocal()

# ---- create students ----
s1 = Student(username="kavya", name="Kavya Mehndiratta")
s2 = Student(username="rahul", name="Rahul Sharma")

# ---- create skills ----
skill1 = Skill(skill_name="Python")
skill2 = Skill(skill_name="SQL")

# ---- create roles ----
role1 = Role(role_name="Backend Developer")
role2 = Role(role_name="Team Lead")

db.add_all([s1, s2, skill1, skill2, role1, role2])
db.commit()

# ---- assign skills ----
db.add_all([
    StudentSkill(username="kavya", skill_id=skill1.skill_id),
    StudentSkill(username="kavya", skill_id=skill2.skill_id),
    StudentSkill(username="rahul", skill_id=skill2.skill_id),
])

# ---- assign roles ----
db.add_all([
    StudentRole(username="kavya", role_id=role1.role_id),
    StudentRole(username="rahul", role_id=role2.role_id),
])

db.commit()
db.close()

print("Sample data inserted successfully")
