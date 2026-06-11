from pydantic import BaseModel


class UpdateCodeRequest(BaseModel):
    code: str