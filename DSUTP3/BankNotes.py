
#pydantic- provide user friendly errors when data is invalid
from pydantic import BaseModel

class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float 