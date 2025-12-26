from __future__ import annotations
from dataclasses import dataclass, field
from typing import Dict, List

@dataclass
class Session:
    user_id: str
    history: List[str] = field(default_factory=list)


# in-memory sessions (MVP)
_sessions: Dict[str, Session] = {}


def get_session(user_id: str) -> Session:
    if user_id not in _sessions:
        _sessions[user_id] = Session(user_id=user_id)
    return _sessions[user_id]