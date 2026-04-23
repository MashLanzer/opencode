---
tags: [integracion, readwise, lectura]
creado: 2026-04-23
actualizado: 2026-04-23
---

# Readwise - Memoria de Lectura

## Descripcion
Sincroniza tus highlights de libros, articulos y web directamente al vault.

## Como Instalar
1. Settings ? Community Plugins
2. Buscar " Readwise Official\
3. Instalar y activar

## Configuracion
1. Ir a readwise.io/dashboard
2. Settings ? Export ? Obsidian
3. Copiar API token
4. Pegar en plugin de Obsidian

## Templates

### Highlight Basico
\\\markdown
---
tags: [highlight, {{category}}]
author: {{author}}
source: {{source_title}}
date: {{highlighted_at}}
---

# {{highlight}}

> {{text}}

## Notas propias
{{personal_note}}
\\\

### Highlight Completo
\\\markdown
---
tags: [highlight, {{category}}]
author: {{author}}
source_title: {{source_title}}
source_url: {{url}}
date: {{highlighted_at}}
highlighted_at: {{highlighted_at}}
color: {{color}}
---

# {{source_title}}

> {{text}}

### Contexto
{{context}}

### Notas
{{personal_note}}

---

*Leido: {{highlighted_at}}*
\\\

## Categorias Soportadas
- book
- article
- tweet
- podcast
- pdf
- video

## Auto-Sync
Configurar en plugin:
- Al abrir Obsidian
- Cada 1 hora
- Cada 12 horas
- Cada 24 horas

## Notas Generadas
- [[Notas/lectura/libros]] - Highlights de libros
- [[Notas/lectura/articulos]] - Articulos
- [[Notas/lectura/tweets]] - Tweets

## Querys Dataview

### Todos los highlights recientes
\\\dataview
TABLE date, source_title as Fuente, text as Highlight
FROM Notas/lectura
WHERE date > date(today) - 30days
SORT date DESC
\\\

### Por categoria
\\\dataview
TABLE date, source_title
FROM Notas/lectura
WHERE contains(tags, book)
SORT date DESC
\\\

---
*Esperando configuracion*