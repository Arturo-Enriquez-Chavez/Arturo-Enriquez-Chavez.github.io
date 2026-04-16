# Portfolio Arturo Enriquez v2.0

Portfolio profesional con sistema de contactos integrado, construido con FastAPI y Bootstrap 5.

## Características

- Diseño premium dark glassmorphism 2026
- Animaciones suaves con AOS.js
- Sistema de contactos con base de datos SQLite
- Botón flotante de WhatsApp
- Panel de administración para gestionar mensajes
- Formulario con validación en tiempo real
- Animación de contadores
- Typing effect en el hero
- Scroll progress bar
- Fully responsive

## Requisitos

- Python 3.10+
- pip

## Instalación

1. Clonar o descargar el proyecto
2. Crear entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Uso

1. Iniciar el servidor:

```bash
python server.py
```

2. Abrir en el navegador:

- **Portfolio:** http://localhost:8000
- **Admin Panel:** http://localhost:8000/admin

## Estructura del Proyecto

```
├── server.py           # Servidor FastAPI
├── database.py         # Gestión de SQLite
├── requirements.txt    # Dependencias
├── portfolio.db        # Base de datos (se crea automáticamente)
├── templates/
│   ├── index.html      # Página principal
│   └── admin.html      # Panel de administración
└── static/
    ├── css/
    │   └── styles.css  # Estilos personalizados
    └── js/
        └── main.js     # JavaScript
```

## API Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Página principal |
| GET | `/admin` | Panel de administración |
| GET | `/api/contacts` | Listar todos los contactos |
| POST | `/api/contact` | Crear nuevo contacto |
| PATCH | `/api/contacts/{id}/read` | Marcar como leído |
| DELETE | `/api/contacts/{id}` | Eliminar contacto |
| GET | `/api/stats` | Estadísticas |

## Base de Datos

SQLite se utiliza para almacenar los mensajes de contacto:

- `id`: ID único
- `name`: Nombre del contacto
- `email`: Correo electrónico
- `subject`: Asunto (opcional)
- `message`: Mensaje
- `phone`: Teléfono (opcional)
- `company`: Empresa (opcional)
- `ip_address`: IP del visitante
- `created_at`: Fecha de creación
- `is_read`: Estado de lectura

## Personalización

### Cambiar número de WhatsApp

Editar en `templates/index.html`:

```html
<a href="https://wa.me/51987654321?text=...">
```

### Cambiar información de contacto

Editar en `templates/index.html` la sección de contacto.

### Agregar CV para descarga

Colocar el archivo PDF en `static/cv-arturo-enriquez.pdf`

## Despliegue

### Producción con Uvicorn

```bash
uvicorn server:app --host 0.0.0.0 --port 8000 --workers 4
```

### Docker (opcional)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Tecnologías

- **Backend:** FastAPI, Pydantic, SQLite
- **Frontend:** Bootstrap 5.3, AOS.js, Vanilla JS
- **UI:** Glassmorphism, CSS Variables, Flexbox/Grid
- **Iconos:** Bootstrap Icons

## Licencia

© 2026 Arturo Enriquez. Todos los derechos reservados.
