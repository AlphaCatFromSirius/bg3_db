from sqlalchemy import text
from database import engine, SessionLocal


session = SessionLocal()
session.execute(text("COPY weapon FROM '/tmp/weapon.csv' DELIMITER ','"))
session.commit()
session.close()
