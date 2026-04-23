---
tags: [analytics, sistema]
creado: 2026-04-23
actualizado: 2026-04-23
---

# Analytics de Progreso

## Descripcion
Estadisticas de implementaciones, tareas y sesiones.

## M�tricas

### Implementaciones
| Semana | Completadas |
|--------|----------|
| 2026-W17 | 11+ |

### Tareas
| Estado | Cantidad |
|--------|---------|
| Completadas | X |
| Pendientes | X |
| En Proceso | X |

### Sesiones
| Fecha | Duracion | Cambios |
|-------|---------|--------|
| 2026-04-23 | ~2hrs | 11+ files |

## Queries Dataview

### Implementaciones por semana
\\\dataview
TABLE created as  Fecha, file.tags as Tags
FROM Notas
WHERE contains(file.tags, implementacion)
SORT created DESC
\\\

### Tareas por estado
\\\dataview
TASK FROM Notas/tareas
WHERE !completed
\\\

### sesiones por fecha
\\\dataview
TABLE date(created) as Fecha, length(file.inlinks) as Links
FROM Notas
WHERE contains(file.tags, conversaciones)
SORT created DESC
\\\

## Como Ver
- [[Notas/tareas/completadas]] -> Completadas
- [[Notas/tareas/pendientes]] -> Pendientes
- GitHub commits -> Actividad

---
*Sistema de analytics*