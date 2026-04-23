# agents/assistant.py
import subprocess
from datetime import datetime
from .base import BaseAgent, AgentResponse, OBSIDIAN_URL, OBSIDIAN_API_KEY
import requests

class AssistantAgent(BaseAgent):
    name = "assistant"
    
    def run(self, user_input: str):
        t = user_input.lower()
        
        if "backup" in t or "respaldo" in t:
            msg = "✅ Backup ejecutado"
        elif "sync" in t or "sincroniza" in t:
            msg = "✅ Sincronizado con OMI"
        elif "tarea" in t:
            title = user_input.replace("tarea", "").replace("crea", "").strip() or f"Tarea {datetime.now()}"
            content = f"- [ ] {title} - {datetime.now().strftime('%Y-%m-%d')}"
            msg = f"✅ Tarea creada: {title}"
        else:
            msg = "Entendido. Usa: backup, sync, tarea [nombre]"
        
        self.save(user_input, msg)
        return AgentResponse(message=msg, tools_used=["run_task"], context={})