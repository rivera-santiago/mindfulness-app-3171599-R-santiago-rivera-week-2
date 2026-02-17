from fastapi import FastAPI, HTTPException
from datetime import datetime
from models import SessionCreate, SessionResponse, SessionUpdate
from database import db_sessions

app = FastAPI(title="Meditation API")

# QUÉ: Crear sesión
# PARA: Registrar sesiones nuevas
# IMPACTO: CRUD - CREATE
@app.post("/sessions/", response_model=SessionResponse)
def create_session(session: SessionCreate):
    new_session = session.model_dump()
    new_session["id"] = len(db_sessions) + 1
    new_session["created_at"] = datetime.utcnow()
    new_session["updated_at"] = None
    db_sessions.append(new_session)
    return new_session


@app.get("/sessions/", response_model=list[SessionResponse])
def list_sessions(skip: int = 0, limit: int = 10):
    return db_sessions[skip: skip + limit]


@app.get("/sessions/{session_id}", response_model=SessionResponse)
def get_session(session_id: int):
    for s in db_sessions:
        if s["id"] == session_id:
            return s
    raise HTTPException(status_code=404, detail="Session not found")


@app.patch("/sessions/{session_id}", response_model=SessionResponse)
def update_session(session_id: int, data: SessionUpdate):
    for s in db_sessions:
        if s["id"] == session_id:
            for k, v in data.model_dump(exclude_unset=True).items():
                s[k] = v
            s["updated_at"] = datetime.utcnow()
            return s
    raise HTTPException(status_code=404, detail="Session not found")


@app.delete("/sessions/{session_id}")
def delete_session(session_id: int):
    global db_sessions
    db_sessions = [s for s in db_sessions if s["id"] != session_id]
    return {"message": "Session deleted"}
