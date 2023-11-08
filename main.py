from auth.database import User

from datetime import datetime
from enum import Enum
from typing import Optional

from fastapi import FastAPI
from fastapi_users import FastAPIUsers
from pydantic import BaseModel, Field

from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.shemas import UserRead, UserCreate

app = FastAPI(
    title='Trading Spp'
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)


fake_users = [
    {'id': 1, 'role': 'Admin', 'name': 'Bob'},
    {'id': 2, 'role': 'investor', 'name': 'John'},
    {'id': 3, 'role': 'trader', 'name': 'Matt'},
]


class DegreeType(Enum):
    newbie = 'newbie'
    expert = 'expert'


class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType


class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[list[Degree]] = []


@app.get('/users/{user_id}', response_model=list[User])
def get_user(user_id: int) -> list[dict]:
    return [user for user in fake_users if user.get('id') == user_id]


fake_traders = [
    {'id': 1, 'user_id': 1, 'currency': 'BTC', 'side': 'buy', 'price': 123, 'amount': 2.12},
    {'id': 2, 'user_id': 1, 'currency': 'BTC', 'side': 'sell', 'price': 125, 'amount': 2.12},
]


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post('/trades')
def add_trades(trades: list[Trade]):
    fake_traders.extend(trades)
    return {'status': 200, 'data': fake_traders}
