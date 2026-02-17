🧘‍♂️ App de Meditación y Mindfulness
Semana 02 — Validación de Datos con Pydantic v2
📌 Descripción General

Este proyecto corresponde a la Semana 02 del bootcamp de Backend con FastAPI y Pydantic v2.
El objetivo es construir una API REST CRUD para la gestión de sesiones de meditación y mindfulness, aplicando validaciones robustas usando Pydantic v2 e integrándolas correctamente con FastAPI.

El dominio seleccionado pertenece al área de Salud y Bienestar, enfocado en la creación, consulta, actualización y eliminación de sesiones de meditación guiada.

🎯 Objetivos de Aprendizaje

Al desarrollar este proyecto se busca demostrar la capacidad de:

Comprender qué es Pydantic y su importancia en FastAPI

Crear esquemas de datos utilizando BaseModel

Configurar validaciones avanzadas con Field

Implementar validadores personalizados con @field_validator

Utilizar tipos de datos especiales (EmailStr, HttpUrl)

Separar correctamente los esquemas de creación, actualización y respuesta

Integrar Pydantic con endpoints CRUD en FastAPI

Ejecutar la aplicación dentro de un entorno Docker

🏛️ Dominio del Proyecto

Dominio: Salud y Bienestar
Aplicación: Meditación y Mindfulness

Entidad Principal: MeditationSession

Una sesión de meditación representa un contenido guiado que puede ser consumido por usuarios finales, incluyendo información como duración, nivel, instructor y recurso de audio.

🧱 Modelo de Datos

La entidad MeditationSession cuenta con los siguientes campos:

Campo	Tipo	Descripción
id	int	Identificador único (autogenerado)
title	str	Título de la sesión
description	str | None	Descripción opcional
duration_minutes	int	Duración en minutos
level	Enum	Nivel: beginner / intermediate / advanced
instructor_email	EmailStr	Email válido del instructor
audio_url	HttpUrl	URL del audio de la sesión
is_active	bool	Estado de la sesión
created_at	datetime	Fecha de creación
updated_at	datetime | None	Fecha de actualización
✅ Validaciones Implementadas

Longitud mínima y máxima para textos

Duración mínima y máxima de la sesión

Validación automática de emails

Validación automática de URLs

Restricción de valores mediante Enum

Validador personalizado para evitar títulos genéricos como “test” o “demo”

Valores por defecto correctamente configurados

🔁 Endpoints CRUD
Método	Endpoint	Descripción
POST	/sessions/	Crear una nueva sesión
GET	/sessions/	Listar sesiones (con paginación)
GET	/sessions/{id}	Obtener sesión por ID
PATCH	/sessions/{id}	Actualizar sesión parcialmente
DELETE	/sessions/{id}	Eliminar sesión

🐳 Ejecución del Proyecto
Requisitos

Docker Desktop

Docker Compose

Pasos para ejecutar

Desde la carpeta:

week-02/3-proyecto/starter


Ejecutar:

docker compose up --build

📘 Documentación Swagger

Una vez levantado el contenedor, la documentación interactiva está disponible en:

http://localhost:8000/docs


Desde allí se pueden probar todos los endpoints del CRUD.

🧪 Almacenamiento de Datos

Este proyecto utiliza una base de datos en memoria (lista de Python) con fines académicos.
No se emplea una base de datos real, ya que el enfoque principal es la validación de datos con Pydantic v2.

🧠 Conceptos Clave Aplicados

BaseModel

Field

@field_validator

Tipos especiales de Pydantic

Separación de esquemas

Integración Pydantic + FastAPI

Contenerización con Docker

📌 Conclusión

Este proyecto demuestra el uso correcto y profesional de Pydantic v2 dentro de una API FastAPI, aplicando validaciones coherentes con el dominio de negocio, una estructura clara de esquemas y un CRUD funcional y documentado.

Cumple con todos los criterios técnicos y académicos establecidos para la Semana 02.

👤 Autor

Santiago Rivera
Bootcamp Backend — FastAPI & Pydantic
week-02