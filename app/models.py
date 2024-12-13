from pydantic import BaseModel
from typing import Optional

class TodoItem(BaseModel):
    id: int
    name: str  # Use 'name' instead of 'title'
    description: str
