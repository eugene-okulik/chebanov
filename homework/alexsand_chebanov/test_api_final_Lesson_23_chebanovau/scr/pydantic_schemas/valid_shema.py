from pydantic import BaseModel, Field, HttpUrl


class MemeShema(BaseModel):
    id: int = Field(gt=0)
    text: str
    url: HttpUrl
    tags: list
    info: object
