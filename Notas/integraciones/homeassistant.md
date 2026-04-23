---
tags: [integracion, homeassistant, iot]
creado: 2026-04-23
actualizado: 2026-04-23
---

# Home Assistant - Integracion

## Descripcion
El sistema reacciona al mundo fisico:
- Notificaciones cuando hay tareas pendientes
- Luces indicadores de estado
- Comandos de voz

## Como Obtener Token
1. Perfil de usuario en Home Assistant
2. Security -> Long-Lived Access Tokens
3. Create token

## Funcionalidades

### Notificaciones
| Trigger | Accion |
|---------|--------|
| Tarea vencida | Notificacion push |
| Nueva tarea alta prioridad | Luz roja |
| Sesion activa | Luz verde |

### Entities
- sensor.opencode_status
- light.opencode_status
- notify.opencode

## Script
- home-assistant-integration.py

## Configuracion de Variable
\\\ash
export HA_TOKEN=tu_token_aqui
export HA_URL=http://homeassistant.local:8123
\\\

## Example
\\\python
from home_assistant_integration import notify_opencode_status

# Notificar cuando hay tareas pendientes
notify_opencode_status( Tienes 3 tareas pendientes)
\\\

---
*Esperando configurar*