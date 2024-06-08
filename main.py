from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from schemas import Note
from database import SessionLocal, engine
from crud import createNote, getNote


app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/ping")
async def index() -> dict[str, str]:
    return {"message": "pong"}

@app.post("/create")
async def create_note(note: Note, db: Session = Depends(get_db)):
    try:
        new_note = createNote(db, data=note)
        return { "note_ID": new_note.id }
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
    

@app.get("/note/{note_ID}")
async def get_note(note_ID: int, db: Session = Depends(get_db)):
    try:
       return getNote(db, note_id=note_ID)
    except Exception as e:
        raise HTTPException(status_code=404, detail=e)