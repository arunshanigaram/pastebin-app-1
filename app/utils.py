import uuid
from datetime import datetime, timedelta

def generate_unique_id():
    return str(uuid.uuid4())

def calculate_expiration(days: int):
    return datetime.utcnow() + timedelta(days=days)