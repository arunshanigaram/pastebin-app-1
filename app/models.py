from sqlalchemy import Column, String, Text, DateTime, Boolean
from datetime import datetime, timedelta
from app.database import Base
import uuid

class Snippet(Base):
    __tablename__ = "snippets"
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    content = Column(Text, nullable=False)
    is_public = Column(Boolean, default=True)
    expires_at = Column(DateTime, nullable=True)