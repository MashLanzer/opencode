---
tags: [export, sistema]
creado: 2026-04-23
---

# Sistema de Export Multi-formato

## Descripcion
Exportar notas a diferentes formatos.

## Formatos Soportados
- Markdown (.md) - Nativo
- HTML (.html) - Web
- PDF (.pdf) - Impresion
- JSON - Estructurado

## Metodos de Export

### 1. OBSIDIAN
- Click derecho > Export
- Markdown to PDF plugin
- Obsidian Shell Commands

### 2. GitHub
- Repo: https://github.com/MashLanzer/opencode
- Export ZIP: descargar repo

### 3. Script (futuro)
\\\powershell
# export-html.ps1
Get-ChildItem -Recurse *.md | ConvertTo-Html
\\\

## Comandos de Export
-  exporta X a html -> Convertir nota
- exporta todo a pdf -> Todo el vault
- descarga backup -> ZIP de GitHub

## Plantillas Exportables
- [[Notas/templates/resumen]] -> PDF
- [[Notas/templates/daily]] -> PDF
- [[Notas/templates/nota]] -> Cualquiera

## Uso
1. Selecciona nota
2. exporta [nota] a [formato]
3. Genero el archivo

---
*Sistema de export*