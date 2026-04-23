# agents/coordinator.py
import uuid
from .memory import AgentMemory

class CoordinatorAgent:
    name = "coordinator"
    
    def __init__(self, model=None):
        from .researcher import ResearchAgent
        from .writer import WriterAgent
        from .assistant import AssistantAgent
        self.subagents = {
            "researcher": ResearchAgent(model),
            "writer": WriterAgent(model),
            "assistant": AssistantAgent(model)
        }
        self.memory = AgentMemory()
    
    def detect_intent(self, text: str) -> str:
        t = text.lower()
        if any(w in t for w in ["busca", "search", "información"]): return "research"
        if any(w in t for w in ["crea", "escribe", "nota"]): return "writer"
        if any(w in t for w in ["backup", "sync", "tarea"]): return "assistant"
        return "assistant"
    
    def run(self, user_input: str):
        intent = self.detect_intent(user_input)
        agent = self.subagents.get(intent)
        if agent:
            result = agent.run(user_input)
            self.memory.add_conversation(self.name, user_input, result.message, {})
            return result
        from .base import AgentResponse
        return AgentResponse(message="OK", tools_used=[], context={})