---
tags: [proyecto, opencode, obsidian, omi]
estado: activo
creado: 2026-04-23
actualizado: 2026-04-23
---

# Proyecto opencode - Memoria Completa

## Descripci�n
Asistente de IA con memoria persistente dual: Obsidian + OMI Second Brain

## Arquitectura

`
         ???????????????
         ?   opencode  ?
         ?   (yo)     ?
    ???????????????????????
    ?         ?          ?
????????? ?????????? ????????
? OMI  ? ?Obsidian? ?GitHub?
? API  ? ? Vault  ? ? Repo ?
????????? ?????????? ????????
`

## Componentes

### 1. Obsidian (Memoria Principal)
- **Puerto**: 27123 (HTTP)
- **API Key**: dadde3d8184... (configurada)
- **Plugins**: Dataview, Tasks
- **Notas**: 15+ notas creadas

### 2. OMI (Segundo Cerebro)
- **API Key**: omi_dev_f109295... (configurada)
- **MCP Key**: omi_mcp_a175e... (configurada)
- **Memorias**: 5+ guardadas
- **Sync**: Autom�tico

### 3. GitHub
- **Repo**: https://github.com/MashLanzer/opencode
- **Commits**: 4+ subidos

---

## Implementaciones Completadas

| # | Implementaci�n | Estado |
|---|---------------|--------|
| 1 | Notas con fecha autom�tica | ? |
| 2 | Sistema de preferencias | ? |
| 3 | Integraci�n Dataview/Tasks | ? |
| 4 | Comandos personalizados | ? |
| 5 | Organizaci�n Obsidian | ? |
| 6 | OMI Second Brain | ? |

---

## Estructura de Notas

`
opencode/
??? Memoria.md              # �ndice
??? Notas/
?   ??? configuracion.md    # Config
?   ??? preferencias.md   # Gustos
?   ??? comandos.md      # Pendiente
?   ??? instrucciones.md  # Gu�a
?   ??? conversaciones.md     # Historial
?   ??? tareas.md        # Progreso
?   ??? instalar-dataview.md  # Gu�a DV
?   ??? 2026-04-23-resumen.md # Resumen
??? Proyectos/
?   ??? opencode.md      # Proyecto
??? sync-to-omi.ps1    # Script
`

---

## C�mo Usar

### Para Hablarme
1. Escribe en [[Notas/comandos.md]] ? secci�n Pendiente
2. O en cualquier nota en [[Notas/]]

### Para Ver Estado
- [[Notas/tareas.md]] - Progreso
- [[Notas/conversaciones.md]] - Historial
- [[Memoria.md]] - �ndice

### Para Sincronizar
`powershell
powershell -File sync-to-omi.ps1
`

---

## Recursos

- GitHub: https://github.com/MashLanzer/opencode
- Memoria: [[Memoria]]
- Config: [[Notas/configuracion]]

*Actualizado: 2026-04-23*