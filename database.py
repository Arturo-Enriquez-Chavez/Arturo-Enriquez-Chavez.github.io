import sqlite3
from datetime import datetime
from typing import List, Optional
from contextlib import contextmanager

DATABASE_PATH = "portfolio.db"

def init_database():
    """Inicializa la base de datos con la tabla de contactos."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                subject TEXT,
                message TEXT NOT NULL,
                phone TEXT,
                company TEXT,
                ip_address TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_read BOOLEAN DEFAULT 0,
                notes TEXT
            )
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_contacts_created_at 
            ON contacts(created_at DESC)
        """)
        cursor.execute("""
            CREATE INDEX IF NOT EXISTS idx_contacts_is_read 
            ON contacts(is_read)
        """)
        conn.commit()

@contextmanager
def get_connection():
    """Context manager para manejar conexiones a la base de datos."""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def save_contact(name: str, email: str, message: str, subject: str = None, 
                 phone: str = None, company: str = None, ip_address: str = None) -> int:
    """Guarda un nuevo contacto en la base de datos."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO contacts (name, email, subject, message, phone, company, ip_address)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (name, email, subject, message, phone, company, ip_address))
        conn.commit()
        return cursor.lastrowid

def get_contacts(limit: int = 50, unread_only: bool = False) -> List[dict]:
    """Obtiene la lista de contactos."""
    with get_connection() as conn:
        cursor = conn.cursor()
        if unread_only:
            cursor.execute("""
                SELECT * FROM contacts 
                WHERE is_read = 0 
                ORDER BY created_at DESC 
                LIMIT ?
            """, (limit,))
        else:
            cursor.execute("""
                SELECT * FROM contacts 
                ORDER BY created_at DESC 
                LIMIT ?
            """, (limit,))
        
        rows = cursor.fetchall()
        return [dict(row) for row in rows]

def get_contact_by_id(contact_id: int) -> Optional[dict]:
    """Obtiene un contacto específico por ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

def mark_contact_as_read(contact_id: int) -> bool:
    """Marca un contacto como leído."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE contacts SET is_read = 1 WHERE id = ?
        """, (contact_id,))
        conn.commit()
        return cursor.rowcount > 0

def get_unread_count() -> int:
    """Obtiene el número de contactos no leídos."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) as count FROM contacts WHERE is_read = 0")
        return cursor.fetchone()["count"]

def delete_contact(contact_id: int) -> bool:
    """Elimina un contacto."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        conn.commit()
        return cursor.rowcount > 0

def search_contacts(query: str) -> List[dict]:
    """Busca contactos por nombre, email o mensaje."""
    with get_connection() as conn:
        cursor = conn.cursor()
        search_term = f"%{query}%"
        cursor.execute("""
            SELECT * FROM contacts 
            WHERE name LIKE ? OR email LIKE ? OR message LIKE ?
            ORDER BY created_at DESC
        """, (search_term, search_term, search_term))
        return [dict(row) for row in cursor.fetchall()]

def get_contact_stats() -> dict:
    """Obtiene estadísticas de contactos."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) as total FROM contacts")
        total = cursor.fetchone()["total"]
        
        cursor.execute("SELECT COUNT(*) as unread FROM contacts WHERE is_read = 0")
        unread = cursor.fetchone()["unread"]
        
        cursor.execute("""
            SELECT COUNT(*) as today FROM contacts 
            WHERE DATE(created_at) = DATE('now')
        """)
        today = cursor.fetchone()["today"]
        
        return {
            "total": total,
            "unread": unread,
            "today": today,
            "read": total - unread
        }
