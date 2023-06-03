from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Song:
    id: int
    name: str
    singer: str
    rating: int

    def __init__(self, id: int, name: str, singer: str, rating: int) -> None:
        self.id = id
        self.name = name
        self.singer = singer
        self.rating = rating

class SongRequest(BaseModel):
    id: Optional[int] = Field(title='id not needed')
    name: str = Field(min_length=3, max_length=10)
    singer: str = Field(min_length=3, max_length=10)
    rating: int = Field(gt=-1, lt=6)
    class Config:
        schema_extra = {
            'example': {
                'name': 'new song',
                'singer': 'Bob',
                'rating': 4
            }
        }


SONGS = [
        Song(1, 'song 1', 'singer 1', 5),
        Song(2, 'song 2', 'singer 2', 4),
        Song(3, 'song 3', 'singer 3', 3),
        Song(4, 'song 4', 'singer 4', 2)
]

@app.get("/songs")
async def get_all_songs():
    return SONGS

@app.post("/songs")
async def add_song(song_request: SongRequest):
    song = Song(**song_request.dict())
    song.id = get_next_song_id()
    SONGS.append(song)


def get_next_song_id() -> int:
    return SONGS[-1].id + 1 if len(SONGS) > 0 else 1
