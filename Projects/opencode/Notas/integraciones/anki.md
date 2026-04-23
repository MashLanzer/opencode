# Anki - Spaced Repetition

## Descripcion
Generar flashcards automaticamente de notas marcadas como aprender.

## Como Instalar
1. Anki app
2. AnkiConnect add-on
3. Puerto 8765

## Scripts
- anki-integration.py

## Uso

```python
from anki_integration import add_notes_from_text

notas = "概念 - 定义"
cards = add_notes_from_text(notas, "OpenCode", "learning")
```

## Workflow
1. Nota con tag aprender
2. Crear tarjetas Q/A
3. AnkiConnect envia

## Tags
- aprender: Para crear flashcards