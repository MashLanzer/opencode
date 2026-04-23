# agents/base.py
import os
import json
import uuid
from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
import requests

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2")
OBSIDIAN_URL = "http://127.0.0.1:27123"
OBSIDIAN_API_KEY = os.getenv("OBSIDIAN_API_KEY")
OMI_API_KEY = os.getenv("OMI_API_KEY")
OMI_API_URL = "https://api-omi.me/v1/dev"

@dataclass
class ToolResult:
    success: bool
    data: Any
    error: str = None

@dataclass
class AgentResponse:
    message: str
    tools_used: List[str]
    context: Dict

class BaseAgent(ABC):
    name: str = "base"
    description: str = "Base agent"
    tools: List[str] = []
    
    def __init__(self, model: str = None):
        self.model = model or OLLAMA_MODEL
        self.conversation_id = str(uuid.uuid4())
        from .memory import AgentMemory
        self.memory = AgentMemory()
    
    def get_note(self, path: str) -> Optional[str]:
        try:
            r = requests.get(f"{OBSIDIAN_URL}/vault/{path}", 
                          headers={"Authorization": f"Bearer {OBSIDIAN_API_KEY}"}, timeout=10)
            return r.text if r.status_code == 200 else None
        except:
            return None
    
    def search_obsidian(self, query: str) -> List[str]:
        try:
            r = requests.get(f"{OBSIDIAN_URL}/vault/", 
                          headers={"Authorization": f"Bearer {OBSIDIAN_API_KEY}"}, timeout=10)
            if r.status_code == 200:
                return [f for f in r.json().get("files", []) if query.lower() in f.lower()]
        except:
            pass
        return []
    
    def get_omi(self, limit: int = 10) -> List[Dict]:
        try:
            r = requests.get(f"{OMI_API_URL}/user/memories?limit={limit}", 
                          headers={"Authorization": f"Bearer {OMI_API_KEY}"}, timeout=10)
            return r.json() if r.status_code == 200 else []
        except:
            pass
        return []
    
    def generate(self, prompt: str) -> str:
        try:
            r = requests.post(f"{OLLAMA_URL}/api/generate", 
                           json={"model": self.model, "prompt": prompt, "stream": False}, timeout=60)
            if r.status_code == 200:
                return r.json().get("response", "")
        except Exception as e:
            print(f"LLM error: {e}")
        return "No disponible"
    
    def save(self, user_msg: str, assistant_msg: str):
        self.memory.add_conversation(self.name, user_msg, assistant_msg, {})
    
    @abstractmethod
    def run(self, user_input: str) -> AgentResponse:
        pass