# opencode

> AI assistant with persistent memory via Obsidian

## Description

opencode is an AI assistant that uses Obsidian as a persistent memory system. It reads and writes notes automatically to maintain context between sessions.

## Features

- Persistent memory with Obsidian vault
- Automatic conversation logging
- Task tracking system
- Organized note structure

## Project Structure

```
opencode/
├── Memoria.md          # Main index
├── Notas/              # General notes
│   ├── configuracion.md
│   └── conversaciones.md
├── Proyectos/          # Project notes
│   └── opencode.md
└── .obsidian/         # Obsidian config (not tracked)
```

## Configuration

See `Notas/configuracion.md` for detailed configuration.

## Usage

1. Start Obsidian with the Local REST API plugin enabled
2. This assistant will automatically read/write memory notes
3. Conversations are saved to `Notas/conversaciones.md`

## License

MIT