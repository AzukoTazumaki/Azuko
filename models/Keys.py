from typing import List, Optional
from sqlmodel import SQLModel, Field, Relationship


class Keys(SQLModel, table=True):
    __tablename__ = 'keys'

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    beat: Optional['Beats'] = Relationship(back_populates='key')
