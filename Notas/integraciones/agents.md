---
tags: [integración, ai, agents]
creado: 2026-04-22
---

# 🤖 AI Agents (Ollama)

| Componente | Estado |
|------------|--------|
| Memory (SQLite) | ✅ |
| Coordinator | ✅ |
| Researcher | ✅ |
| Writer | ✅ |
| Assistant | ✅ |
| Ollama | ⚠️ Docker |

## Uso
```python
from agents import CoordinatorAgent
agent = CoordinatorAgent()
result = agent.run("busca información")
print(result.message)
```

## Setup Ollama
```bash
docker run -d -p 11434:11434 --name ollama ollama/ollama
docker exec ollama ollama pull llama3.2
```

*Updated: 2026-04-22*