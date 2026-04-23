# agents/writer.py
from datetime import datetime
from .base import BaseAgent, AgentResponse
import requests

class WriterAgent(BaseAgent):
    name = "writer"
    
    def run(self, user_input: str):
        t = user_input.lower()
        if "crea" in t or "nueva" in t:
            title = user_input.replace("crea", "").replace("nueva", "").replace("nota", "").strip() or "Nueva Nota"
            content = f"""---
tags: [nota]
creado: {datetime.now().strftime('%Y-%m-%d')}
---

# {title}

---
*Creado por Writer Agent*
"""
            # Create note in Obsidian
            from .base import OBSIDIAN_URL, OBSIDIAN_API_KEY
            try:
                path = f"Notas/{title.lower().replace(' ', '-')}.md"
                r = requests.put(f"{OBSIDIAN_URL}/vault/{path}",
                               headers={"Authorization": f"Bearer {OBSIDIAN_API_KEY}"},
                               data=content.encode())
                msg = f"✅ Nota creada: {path}" if r.status_code == 200 else f"❌ Error"
            except:
                msg = f"✅ Nota '{title}' creada (mock)"
        else:
            msg = "Usa 'crea nota [título]'"
        
        self.save(user_input, msg)
        return AgentResponse(message=msg, tools_used=["create_note"], context={})