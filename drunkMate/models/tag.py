from sqlmodel import SQLModel, Field


class Tag(SQLModel):
    name: str = Field(unique=True, min_length=1, max_length=50)
