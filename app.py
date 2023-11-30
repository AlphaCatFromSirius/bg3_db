from fastapi import FastAPI, Depends
from database import SessionLocal
from crud import get_weapon, get_weapons
from schema import Weapon
from sqlalchemy.orm import Session


app = FastAPI()
session = SessionLocal()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def start_page() -> dict:
    return {'message': "Welcome to Baldur's Gate weapon base"}


@app.get('/weapons/', response_model=list[Weapon])
def get_all_weapons(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    weapon = get_weapons(db, offset, limit)
    return weapon


@app.get('/weapons/', response_model=Weapon)
def get_weapon(name: str, db: Session = Depends(get_db)):
    weapon = get_weapon(db, name)
    return weapon
