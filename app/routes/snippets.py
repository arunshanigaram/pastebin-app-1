from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, dependencies

router = APIRouter(prefix="/snippets", tags=["snippets"])

@router.post("/", response_model=schemas.SnippetResponse)
def create_snippet(snippet: schemas.SnippetCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_snippet(db=db, snippet=snippet)

@router.get("/{snippet_id}", response_model=schemas.SnippetResponse)
def get_snippet(snippet_id: str, db: Session = Depends(dependencies.get_db)):
    snippet = crud.get_snippet(db, snippet_id)
    if snippet is None:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet