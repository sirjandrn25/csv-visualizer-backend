from pydantic import BaseModel
class CsvFileBase(BaseModel):
    title: str
    description:str
    file_url:str
    user_id:str | None

class CsvFileCreate(CsvFileBase):
    pass
class CsvFile(CsvFileBase):
    id: int
    user_id: int
    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
class UserCreate(UserBase):
    password: str
class User(UserBase):
    id: int
    is_active: bool
    files: list[CsvFile] = []

    class Config:
        orm_mode = True

