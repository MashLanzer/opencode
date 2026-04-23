# Memoria - opencode

## 🤖 Asistente IA con Memoria Persistente

> Sistema completo: 25+ implementaciones + 7 integraciones externas

---

## 📋 ÍNDICE PRINCIPAL

### 🏠 Sistema Core
- [[Notas/daily-brief|Daily Brief]] - Resumen diario (MUESTRA SIEMPRE AL INICIAR)
- [[Notas/tareas/pendientes|Tareas Pendientes]] - Lista de tareas
- [[Notas/tareas/completadas|Completadas]] - Historial
- [[Notas/alertas|Alertas]] - Notificaciones del sistema

### 💾 Memoria y Contexto
- [[Notas/conversaciones|Conversaciones]] - Historial de sesiones
- [[Notas/temas|Temas]] - Temas activos de conversación
- [[Notas/chat-context|Contexto de Chat]] - Continuidad entre sesiones
- [[Notas/preferencias|Preferencias]] - Tus preferencias

### 🔍 Búsqueda y Utilidades
- [[Notas/busqueda|Búsqueda Cruzada]] - Buscar en Obsidian + OMI
- [[Notas/analytics|Analytics]] - Estadísticas del proyecto
- [[Notas/export|Export]] - Exportar notas

### 📅 Calendario y Tiempo
- [[Notas/calendario|Calendario]] - Fechas límite
- [[Notas/templates/fecha|Plantilla Fecha]]

### 📝 Plantillas
- [[Notas/templates/index|Índice de Plantillas]]
- [[Notas/templates/tarea|Nueva Tarea]]
- [[Notas/templates/proyecto|Nuevo Proyecto]]
- [[Notas/templates/daily|Daily Note]]
- [[Notas/templates/resumen|Resumen de Sesión]]

### 🔄 Respaldos
- [[Notas/backup/historial|Historial de Backups]]
- [[backup.ps1|Script de Backup]]

---

## 🔌 INTEGRACIONES

### Mensajería
- [[Notas/integraciones/telegram|Telegram Bot]] - Bot de Telegram

### Productividad
- [[Notas/integraciones/cal|Cal.com]] - Calendario
- [[Notas/integraciones/proyectos|Linear/Notion]] - Gestión de proyectos

### Lectura
- [[Notas/integraciones/readwise|Readwise]] - Highlights de libros

### Web
- [[browser-extension|Web Clipper]] - Extension de navegador

### IoT
- [[Notas/integraciones/homeassistant|Home Assistant]] - Casa inteligente

### Aprendizaje
- [[Notas/integraciones/anki|Anki]] - Spaced Repetition

---

## 📊 RESÚMENES

- [[Notas/implementaciones|Todas las Implementaciones]]
- [[Notas/integraciones/progreso|Progreso de Integraciones]]
- [[Notas/configuracion|Configuración Técnica]]

---

## 🐙 GITHUB

**Repo:** https://github.com/MashLanzer/opencode

### Archivos Principales
```
/telegram-bot.py      - Bot de Telegram
/cal-integration.py   - Calendario
/anki-integration.py - Anki
/home-assistant-integration.py
/linear-notion-integration.py
/Dockerfile
/requirements.txt
/browser-extension/
```

---

## ⚙️ ESTADO DEL SISTEMA

| Componente | Estado |
|------------|---------|
| Obsidian Vault | ✅ Activo |
| OMI Second Brain | ✅ Sincronizado |
| GitHub | ✅ Subido |
| Telegram Bot | ✅ Listo |
| Cal.com | ✅ Configurado |

---

## 🚀 FLUJO DE TRABAJO

### Al Iniciar Sesión
1. Leo [[Notas/daily-brief|Daily Brief]]
2. Leo [[Notas/tareas/pendientes|Tareas]]
3. Leo [[Notas/alertas|Alertas]]
4. Leo OMI memories

### Durante la Sesión
- Guardo temas en [[Notas/conversaciones|conversaciones]]
- Creo notas en [[Notas/|Notas/]]
- Actualizo [[Notas/tareas/pendientes|pendientes]]

### Al Finalizar
- Resumen en [[Notas/conversaciones|conversaciones]]
- Backup con [[backup.ps1|backup.ps1]]
- Sync a OMI

---

*Última actualización: 2026-04-23*
*opencode - Tu segundo cerebro activo*