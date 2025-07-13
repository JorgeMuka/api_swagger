# API con Swagger y Django REST Framework

Este proyecto implementa una API RESTful documentada automáticamente con **drf-yasg** y explorable mediante Swagger UI y ReDoc.

## 🔧 Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- drf-yasg (Swagger y ReDoc)

## 🔗 Accesos locales

- [Swagger UI](http://127.0.0.1:8000/swagger/)
- [ReDoc](http://127.0.0.1:8000/redoc/)

## 🚀 Endpoint disponible

- `GET /api/hello/` → Devuelve un mensaje de saludo en formato JSON.

## 📸 Capturas

### Swagger UI funcionando

![Swagger UI](docs/swagger_ui.png)

### ReDoc funcionando

![ReDoc UI](docs/redoc_ui.png)

## ✅ Descripción del desarrollo

- Se creó un endpoint básico con `APIView` para probar la integración de Swagger.
- Se utilizó el decorador `@swagger_auto_schema` para describir el endpoint.
- El archivo `urls.py` incluye rutas para Swagger y Redoc.
- El sistema fue probado desde la interfaz Swagger sin errores.

## 🧼 Revisión del código

- Código limpio y comentado.
- Imports organizados.
- Funciones claras y ordenadas.

---

> Proyecto realizado como evaluación final de documentación de API con Django REST Framework + Swagger.
