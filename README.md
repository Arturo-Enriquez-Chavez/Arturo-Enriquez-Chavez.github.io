# Arturo Enriquez - Portfolio Profesional

Portfolio profesional de Arturo Enriquez - AI Engineer & Software Architect, especializado en LLM, RAG Systems y arquitecturas SaaS escalables.

## 🌐 Demo en Vivo

[arturo-enriquez.github.io](https://arturo-enriquez.github.io)

## ✨ Características

- **Diseño premium dark glassmorphism 2026**
- **Animaciones suaves con AOS.js**
- **Formulario de contacto con Formspree** (servicio externo)
- **Botón flotante de WhatsApp**
- **Formulario con validación en tiempo real**
- **Animación de contadores**
- **Typing effect en el hero**
- **Scroll progress bar**
- **Fully responsive**

## 📁 Estructura del Proyecto

```
├── index.html          # Página principal
├── static/
│   ├── css/
│   │   └── styles.css  # Estilos personalizados
│   └── js/
│       └── main.js     # JavaScript
└── README.md           # Este archivo
```

## 🚀 Uso Local

1. Clonar el repositorio:
```bash
git clone https://github.com/Arturo-Enriquez-Chavez/Arturo-Enriquez-Chavez.github.io.git
cd Arturo-Enriquez-Chavez.github.io
```

2. Abrir `index.html` directamente en el navegador o usar un servidor local:
```bash
# Python 3
python -m http.server 8000

# Node.js (con http-server)
npx http-server
```

3. Abrir en el navegador: `http://localhost:8000`

## ⚙️ Personalización

### Cambiar número de WhatsApp
Editar en `index.html`:
```html
<a href="https://wa.me/51973082184?text=...">
```

### Configurar Formspree
1. Crear cuenta en [formspree.io](https://formspree.io)
2. Crear un nuevo formulario
3. Reemplazar `YOUR_FORMSPREE_ID` en `index.html` con tu ID:
```html
<form action="https://formspree.io/f/YOUR_FORMSPREE_ID" method="POST">
```

### Cambiar información de contacto
Editar en `index.html` la sección de contacto.

### Agregar CV para descarga
Colocar el archivo PDF en `static/cv-arturo-enriquez.pdf`

## 🛠️ Tecnologías

- **Frontend**: Bootstrap 5.3, AOS.js, Vanilla JS
- **UI**: Glassmorphism, CSS Variables, Flexbox/Grid
- **Iconos**: Bootstrap Icons
- **Hosting**: GitHub Pages

## 📦 Despliegue en GitHub Pages

Este sitio está configurado para desplegarse automáticamente en GitHub Pages. Simplemente:

1. Hacer push a la rama `main`
2. GitHub Pages se despliega automáticamente desde la raíz del repositorio
3. El sitio estará disponible en `https://username.github.io`

## 📝 Licencia

© 2026 Arturo Enriquez. Todos los derechos reservados.
