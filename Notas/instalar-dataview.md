---
estado: por-hacer
 fecha: 2026-04-23
 tags: [plugin, obsidian, dataview]
tipo: integracion
---

# Plugin Dataview - Gu�a de Instalaci�n

## En Obsidian

1. Ve a Settings > Community plugins
2. Busca  Dataview
3. Instala y habilita

## Notas Compatibles

Las notas necesitan frontmatter con tags:

`yaml
---
estado: pendiente
tags: [tarea]
---
`

## Queries de Ejemplo

\\\dataview
TASK FROM Notas
WHERE estado = pendiente
\\\

*Creado: 2026-04-23*