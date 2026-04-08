from pydantic import BaseModel
from typing import List, Optional

class CompilerOptAction(BaseModel):
    direction: str
    reasoning: str

class CompilerOptObservation(BaseModel):
    echoed_message: str
    message_length: int
    done: bool
    reward: float
    current_position: List[int]
    metadata: Optional[dict] = None
