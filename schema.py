from pydantic import BaseModel


class Weapon(BaseModel):
    id: int
    name: str
    damage: str
    rarity: str
    distance: str
    properties: str
    weapon_action: str

    class Config:
        orm_mode = True
