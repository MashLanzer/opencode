---
tags: [busqueda, sistema]
creado: 2026-04-23
---

# Sistema de Busqueda Cruzada

## Descripcion
Buscar en OBSIDIAN + OMI al mismo tiempo.

## Como Usar
Escribe tu busqueda y ejecuto en ambos sistemas.

## Endpoints

### OBSIDIAN
- GET /vault/Notas/{nota}.md

### OMI
- GET /v1/dev/user/memories?q={query}
- GET /v1/dev/user/conversations?q={query}

## Ejemplo de Output
\\\
## Resultados OBSIDIAN
[contenido de notas]

## Resultados OMI
[contenido de memorias]
\\\

## Comandos
-  busca X o search X -> Buscar en ambos
- busca en OBSIDIAN X -> Solo OBSIDIAN
- busca en OMI X -> Solo OMI

---
*Sistema de busqueda cruzada*