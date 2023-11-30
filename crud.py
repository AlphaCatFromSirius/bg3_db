from sqlalchemy.orm import Session
from models import Weapon


def get_weapon(db: Session, name: str):
    return db.query(Weapon).filter(Weapon.name == name).first()


def get_weapons(db: Session, offset: int = 0, limit: int = 0):
    return db.query(Weapon).offset(offset).limit(limit).all()
