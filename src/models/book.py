from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str


class BookIn(BookBase):
    pass


class BookOut(BookBase):
    id: int
