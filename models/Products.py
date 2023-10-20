from typing import Optional
from sqlmodel import SQLModel, Field, Relationship


class Products(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    price: int
    old_price: int | None = None
