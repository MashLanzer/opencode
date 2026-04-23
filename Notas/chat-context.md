---
tags: [chat, contexto]
creado: 2026-04-23
actualizado: 2026-04-23
---

# Chat Context

## Descripcion
Resumen de conversacion actual para continuar entre sesiones.

## Como Funciona
1. Guardo contexto al final de sesion
2. Recupero al inicio de la siguiente
3. Puedo continuar sin repetir

## Estructura
\\\markdown
## Sesion Actual
- Hora inicio: YYYY-MM-DD HH:MM
- Tema principal: X
- Subtemas: [a, b, c]
- Pendientes: [1, 2, 3]
- Ultimo message:  ...

## Historial
### Sesion Anterior
- Tema: X
- Estado: completado/pendiente
\\\

## Actualizar al Final
Cada sesion, actualizo:
- Tema principal
- Subtemas discutidos
- Pendientes para proxima sesion
- Ultimo mensaje del usuario

## Para Continuar
- continuar con X -> Buscar tema
- donde quedamos -> Mostrar contexto
- ultimo tema -> Tema principal

---
*Sistema de chat context*