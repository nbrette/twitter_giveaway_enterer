from pydantic import BaseModel, validator
from models.account_enum import Accounts

class EnterRequest(BaseModel):
    account: str
