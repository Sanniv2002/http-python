from pydantic import BaseModel
from typing import List, Optional


class Note(BaseModel):
    # {
    # "content" : "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut lobortis urna id faucibus lobortis",
    # "linked_entities" : ["Mescaline", "Methamphetamine", "Opioids", "Psilocybin"]
    # }
    name: str
    content: str
    linked_entities: Optional[List[str]] = None  # Optional field