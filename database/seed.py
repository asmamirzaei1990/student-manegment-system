from .database import Database

def seed_database():
    db = Database()
    db.initialize()
    db.seed_if_empty()
    return db
