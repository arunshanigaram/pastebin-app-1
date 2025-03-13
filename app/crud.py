from sqlalchemy.orm import Session
from app import models, schemas

def create_snippet(db: Session, snippet: schemas.SnippetCreate):
    db_snippet = models.Snippet(**snippet.dict())
    db.add(db_snippet)
    db.commit()
    db.refresh(db_snippet)
    return db_snippet

def get_snippet(db: Session, snippet_id: str):
    return db.query(models.Snippet).filter(models.Snippet.id == snippet_id).first()

def update_snippet(db: Session, snippet_id: str, snippet: schemas.SnippetCreate):
    db_snippet = get_snippet(db, snippet_id)
    if db_snippet:
        for key, value in snippet.dict().items():
            setattr(db_snippet, key, value)
        db.commit()
        db.refresh(db_snippet)
    return db_snippet

def delete_snippet(db: Session, snippet_id: str):
    db_snippet = get_snippet(db, snippet_id)
    if db_snippet:
        db.delete(db_snippet)
        db.commit()
    return db_snippet