from pydantic import BaseModel


class PositionListResponse(BaseModel):
    id: int
    name: str


class PositionInsertRequest(BaseModel):
    name: str


class PositionUpdateRequest(BaseModel):
    name: str
