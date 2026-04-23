---
tags: [tareas, sistema]
creado: 2026-04-23
actualizado: 2026-04-23
---

# Sistema de Tareas Completas

## Descripci�n
Sistema de tareas con contexto completo: crear ? hacer ? completar

## Carpetas
- [[Notas/tareas/pendientes]] - Tareas por hacer
- [[Notas/tareas/completadas]] - Tareas completadas
- [[Notas/tareas/proceso]] - Tareas en proceso

## C�mo Crear una Tarea
Usa la plantilla [[Notas/templates/tarea]]

## Formato de Tarea
- [ ] Nombre de tarea
  - contexto: raz�n o detalle
  - prioridad: alta|media|baja
  - fecha-creacion: YYYY-MM-DD
  - fecha-limite: YYYY-MM-DD

## Queries (Dataview)
\\\dataview
TASK FROM  Notas/tareas
WHERE !completed
SORT fecha-creacion desc
\\\

## Estado
\\\dataview
TASK FROM Notas/tareas
WHERE completed
SORT done after today -7days
\\\

---
*Sistema de tareas*