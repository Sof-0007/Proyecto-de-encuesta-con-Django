# 🧠 Sitio Web - Inteligencia Artificial y Redes Neuronales

Un sitio web educativo construido con Django que proporciona información completa sobre Inteligencia Artificial y Redes Neuronales Artificiales.

## 🚀 Características

### Landing Page
- Diseño moderno con gradientes tecnológicos
- Navegación clara
- Botones de inicio de sesión y registro
- Información sobre el contenido educativo
- Footer con enlaces y redes sociales

### Sistema de Autenticación
- Registro de nuevos usuarios con validación
- Inicio de sesión seguro
- Protección de páginas privadas
- Redirección automática después del login

### Dashboard Privado
El dashboard incluye tres secciones principales:

#### Sección A: Definición de Inteligencia Artificial
- Definiciones de 3 autores destacados:
  - John McCarthy
  - Stuart Russell y Peter Norvig
  - Marvin Minsky
- Tarjetas visuales modernas
- Información del año/referencia

#### Sección B: Definición de Redes Neuronales Artificiales
- Explicación de qué son las redes neuronales
- Cómo funcionan
- Relación con el cerebro humano
- Uso dentro de la IA
- Tarjetas informativas

#### Sección C: Tipos de Redes Neuronales
Clasificación visual de 7 tipos principales:
- Perceptrón
- Redes Feedforward
- Redes Convolucionales (CNN)
- Redes Recurrentes (RNN)
- LSTM
- GANs
- Transformers

Cada tipo incluye:
- Nombre
- Descripción breve
- Casos de uso
- Ícono representativo

## 💻 Diseño y Experiencia

- **Interfaz Moderna**: Dashboard tipo panel de control
- **Responsive**: Optimizado para PC y móvil
- **Animaciones**: Efectos suaves y transiciones
- **Paleta de Colores Tecnológica**: Azules, violetas, negros y blancos
- **Tarjetas Modernas**: Con sombras y bordes redondeados
- **Íconos Tecnológicos**: FontAwesome integrado
- **Sidebar Dinámico**: Menú lateral inteligente

## 🛠️ Configuración y Uso

### Requisitos Previos
- Python 3.8+
- Django 5.1.4

### Instalación

1. **Navegar al directorio del proyecto**:
```bash
cd djangotutorial
```

2. **Crear y activar entorno virtual**:
```bash
python -m venv venv
source venv/Scripts/activate  # En Windows
```

3. **Instalar dependencias**:
```bash
pip install django
```

4. **Aplicar migraciones** (si es necesario):
```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Poblar datos iniciales**:
```bash
python populate_db.py
```

6. **Crear superusuario** (si no existe):
```bash
python manage.py createsuperuser
```

### Ejecutar el Servidor

```bash
python manage.py runserver
```

Accede a:
- **Landing Page**: http://localhost:8000/
- **Admin**: http://localhost:8000/admin/

### Credenciales de Demostración
- **Usuario Admin**: admin
- **Contraseña**: admin123

## 📁 Estructura del Proyecto

```
djangotutorial/
├── core/                          # App principal
│   ├── migrations/               # Migraciones de BD
│   ├── templates/core/           # Templates de la app
│   │   ├── landing.html         # Página principal
│   │   ├── login.html           # Formulario de login
│   │   ├── register.html        # Formulario de registro
│   │   └── dashboard.html       # Dashboard privado
│   ├── static/                  # Archivos estáticos
│   ├── admin.py                 # Configuración del admin
│   ├── models.py                # Modelos (AIAuthor, NeuralNetworkType)
│   ├── views.py                 # Vistas principales
│   └── urls.py                  # URLs de la app
├── mysite/                       # Configuración del proyecto
│   ├── settings.py              # Configuración de Django
│   ├── urls.py                  # URLs principales
│   └── wsgi.py
├── templates/
│   └── base.html                # Template base con navegación
├── static/                       # Archivos estáticos del proyecto
├── manage.py                    # Gestor de Django
├── populate_db.py               # Script para poblar datos
└── db.sqlite3                   # Base de datos SQLite

```

## 📊 Modelos de Base de Datos

### AIAuthor
- `name`: Nombre del autor
- `definition`: Definición de IA según el autor
- `year`: Año o referencia aproximada

### NeuralNetworkType
- `name`: Nombre del tipo de red neuronal
- `description`: Descripción detallada
- `use_case`: Casos de uso principales
- `icon`: Ícono representativo (FontAwesome)

## 🎨 Paleta de Colores

- **Primario**: #6366f1 (Indigo)
- **Secundario**: #8b5cf6 (Violeta)
- **Acento**: #a78bfa (Violeta claro)
- **Oscuro**: #1e293b (Negro azulado)
- **Claro**: #f1f5f9 (Blanco grisáceo)

## 🔐 Seguridad

- Protección CSRF integrada
- Autenticación de usuario requerida para el dashboard
- Validación de formularios
- Passwords hasheados con algoritmo seguro
- Middleware de seguridad de Django activado

## 🚀 Próximas Mejoras

- [ ] Implementar autenticación OAuth (Google, GitHub)
- [ ] Agregar un sistema de comentarios
- [ ] Crear un blog educativo
- [ ] Implementar cuestionarios interactivos
- [ ] Agregar certificados digitales
- [ ] Sistema de búsqueda avanzada
- [ ] Implementar sistema de favoritos

## 📝 Licencia

Este proyecto está disponible bajo la licencia MIT.

## 👤 Autor

Proyecto educativo desarrollado con Django y Copilot.

---

**Disfruta aprendiendo sobre Inteligencia Artificial y Redes Neuronales Artificiales!** 🧠✨
