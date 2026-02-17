from pydantic import BaseModel, Field, EmailStr, HttpUrl
from datetime import datetime
from enum import Enum

# QUÉ: Enum de niveles
# PARA: Limitar valores posibles
# IMPACTO: Evita datos inválidos
class LevelEnum(str, Enum):
    beginner = "beginner"
    intermediate = "intermediate"
    advanced = "advanced"


class SessionBase(BaseModel):
    title: str = Field(min_length=3, max_length=100)
    description: str | None = None
    duration_minutes: int = Field(ge=5, le=180)
    level: LevelEnum
    instructor_email: EmailStr
    audio_url: HttpUrl
    is_active: bool = True


class SessionCreate(SessionBase):
    pass


class SessionUpdate(BaseModel):
    title: str | None = None
    duration_minutes: int | None = None
    is_active: bool | None = None


class SessionResponse(SessionBase):
    id: int
    created_at: datetime
    updated_at: datetime | None = None
