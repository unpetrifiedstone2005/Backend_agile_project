from src.database_2.db import engine
from src.database_2.base import Base
from src.database_2 import models

print("ENGINE URL:", engine.url)

Base.metadata.create_all(bind=engine)
print("TABLES CREATED")
