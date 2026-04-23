---
tags: [alertas, sistema]
creado: 2026-04-23
actualizado: 2026-04-23
---

# Sistema de Alertas

## Descripcion
Notificaciones de tareas atrasadas, alertas de pendientes importantes.

## Como Funciona
Al iniciar sesion, verifico:
1. Tareas atrasadas (fecha-limite < hoy)
2. Recordatorios para hoy
3. Tareas con prioridad alta sin completar

## Tipos de Alerta

### Alerta Roja (Atrasada)
\\\dataview
TASK FROM  Notas
WHERE fecha-limite < date(today)
SORT fecha-limite
\\\

### Alerta Amarilla (Recordatorio Hoy)
\\\dataview
TASK FROM Notas
WHERE recordatorio = date(today)
\\\

### Alerta Naranja (Prioridad Alta)
\\\dataview
TASK FROM Notas
WHERE prioridad = alta AND !completed
\\\

## Formato de Alerta en Nota
\\\markdown
- [ ] Tarea importante
  prioridad: alta
  fecha-limite: 2026-04-30
  alerta: true
\\\

## Output al Iniciar
\\\
=== ALERTAS ===

[Rojo] 3 tareas atrasadas
[Amarillo] 2 recordatorios hoy
[Naranja] 1 tarea prioritaria

=== FIN ALERTAS ===
\\\

---
*Sistema de alertas*