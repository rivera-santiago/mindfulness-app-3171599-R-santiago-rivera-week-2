from datetime import datetime

# QUÉ: Base de datos en memoria
# PARA: Almacenar sesiones de meditación sin usar una DB real
# IMPACTO: Permite desarrollar y probar el CRUD completo
db_sessions: list[dict] = []
