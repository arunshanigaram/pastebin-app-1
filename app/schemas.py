from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class SnippetCreate(BaseModel):
    content: str
    is_public: bool
    expires_at: Optional[datetime] = None

class SnippetResponse(SnippetCreate):
    id: str

    model_config = {
        "from_attributes": True
    }
