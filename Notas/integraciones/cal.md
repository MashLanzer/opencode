---
tags: [integracion, cal, calendario]
creado: 2026-04-23
actualizado: 2026-04-23
---

# Cal.com - Integracion de Calendario

## Configuracion
- **API Key**: cal_live_9643088a06b3a5a774337b5e40485f93

## Estado
- **API**: Conectada
- **Calendarios**: 0 (sin conectar)
- **Event Types**: 0

## Pendiente
- [ ] Conectar calendario en Cal.com
- [ ] Autorizar Google Calendar u Outlook

## Como Conectar
1. Ir a cal.com/settings
2. Connected Calendars
3. Add Calendar (Google/Outlook)
4. Autorizar

## Funcionalidades
- Leer reuniones del dia
- Ver disponibilidad
- Agendar reuniones
- Preparar contexto para reuniones

## Scripts
- cal-integration.py

## Uso
\\\python
from cal_integration import check_today_meetings, get_bookings

# Get today meetings
meetings = check_today_meetings()
for meeting in meetings:
    print(meeting[title])
\\\

---
*Esperando conectar calendario*