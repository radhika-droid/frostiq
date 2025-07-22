from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class Favorite(BaseModel):
    id: Optional[int] = None  # Optional, will be filled when returning data
    user_id: int
    item_id: int
    item_name: str
