---
tags: [calendario, sistema]
creado: 2026-04-23
actualizado: 2026-04-23
---

# Sistema de Calendario

## Descripcion
Tareas con fechas limite, recordatorios y vinculo con periodic notes.

## Uso
Agregar fecha-limite a cualquier tarea:
\\\markdown
- [ ] Tarea pendiente
  fecha-limite: 2026-04-30
  recordatorio: 2026-04-28
\\\

## Queries �tiles

### Tareas por hacer esta semana
\\\dataview
TASK FROM  Notas
WHERE fecha-limite <= date(today) + 7days
SORT fecha-limite
\\\

### Tareas atrasadas
\\\dataview
TASK FROM Notas
WHERE fecha-limite < date(today)
SORT fecha-limite
\\\

### Con recordatorio
\\\dataview
TASK FROM Notas
WHERE recordatorio = date(today)
\\\

## Periodic Notes
- [[Notas/daily]] usa formato YYYY-MM-DD
- Plantilla [[Notas/templates/daily]]

## Notas con Fechas
- [[Notas/daily-brief.md]] - Daily actual
- [[Notas/YYYY-MM-dd-resumen.md]] - Resumenes

---
*Sistema de calendario*