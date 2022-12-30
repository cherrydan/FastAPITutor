from typing import List

from pydantic import BaseModel
from datetime import date


class Genres(BaseModel):
    name: str


class AudioBook(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genres]
    pages: int
