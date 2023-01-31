from pydantic import BaseModel

class EnterRequest(BaseModel):
    account: str
