from sqlalchemy.orm import Session

from models import Notes
from schemas import Note

def getNote(db: Session, note_id: int):
    return db.query(Notes).filter(Notes.id == note_id).first()


def createNote(db: Session, data: Note):
    db_note = Notes(name=data.name, content=data.content, linked_entities=data.linked_entities)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note