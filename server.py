from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
from datetime import datetime
import database

app = FastAPI(
    title="Portfolio API - Arturo Enriquez",
    description="API para el portfolio profesional con sistema de contactos",
    version="2.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

database.init_database()

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    message: str
    subject: Optional[str] = None
    phone: Optional[str] = None
    company: Optional[str] = None
    
    @field_validator('name')
    @classmethod
    def name_not_empty(cls, v):
        if not v or len(v.strip()) < 2:
            raise ValueError('El nombre debe tener al menos 2 caracteres')
        return v.strip()
    
    @field_validator('message')
    @classmethod
    def message_not_empty(cls, v):
        if not v or len(v.strip()) < 10:
            raise ValueError('El mensaje debe tener al menos 10 caracteres')
        return v.strip()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Sirve la página principal del portfolio."""
    stats = database.get_contact_stats()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "stats": stats}
    )

@app.get("/admin", response_class=HTMLResponse)
async def admin_panel(request: Request):
    """Panel de administración de contactos."""
    contacts = database.get_contacts()
    stats = database.get_contact_stats()
    return templates.TemplateResponse(
        "admin.html",
        {"request": request, "contacts": contacts, "stats": stats}
    )

@app.get("/api/contacts")
async def get_contacts_api(unread_only: bool = False):
    """API para obtener contactos."""
    contacts = database.get_contacts(unread_only=unread_only)
    for contact in contacts:
        contact['created_at'] = str(contact['created_at'])
    return {"contacts": contacts, "stats": database.get_contact_stats()}

@app.post("/api/contact")
async def create_contact(request: Request, form_data: ContactForm):
    """API para crear un nuevo contacto."""
    try:
        client_ip = request.client.host if request.client else None
        contact_id = database.save_contact(
            name=form_data.name,
            email=form_data.email,
            message=form_data.message,
            subject=form_data.subject,
            phone=form_data.phone,
            company=form_data.company,
            ip_address=client_ip
        )
        return {
            "success": True,
            "message": "Mensaje enviado correctamente",
            "contact_id": contact_id
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.patch("/api/contacts/{contact_id}/read")
async def mark_as_read(contact_id: int):
    """Marca un contacto como leído."""
    if database.mark_contact_as_read(contact_id):
        return {"success": True, "message": "Marcado como leído"}
    raise HTTPException(status_code=404, detail="Contacto no encontrado")

@app.delete("/api/contacts/{contact_id}")
async def delete_contact_api(contact_id: int):
    """Elimina un contacto."""
    if database.delete_contact(contact_id):
        return {"success": True, "message": "Contacto eliminado"}
    raise HTTPException(status_code=404, detail="Contacto no encontrado")

@app.get("/api/stats")
async def get_stats():
    """Obtiene estadísticas de contactos."""
    return database.get_contact_stats()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
