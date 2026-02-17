import re
from pydantic import field_validator
from models import SessionBase

# QUÉ: Validador de título
# PARA: Evitar títulos genéricos
# IMPACTO: Mejora calidad del contenido
class SessionValidators(SessionBase):

    @field_validator("title")
    def validate_title(cls, v: str) -> str:
        if re.search(r"(test|demo)", v.lower()):
            raise ValueError("Title cannot contain 'test' or 'demo'")
        return v
