# agents/researcher.py
from .base import BaseAgent, AgentResponse

class ResearchAgent(BaseAgent):
    name = "researcher"
    tools = ["search_obsidian", "get_omi"]
    
    def run(self, user_input: str):
        query = user_input.replace("busca", "").strip()
        obs = self.search_obsidian(query)
        omi = self.get_omi(5)
        
        results = [f"Obsidian: {r}" for r in obs[:5]] if obs else []
        results += [f"OMI: {r.get('content','')[:30]}" for r in omi[:3]] if omi else []
        
        msg = f"Resultados para '{query}':\n" + "\n".join(results) if results else "Sin resultados"
        self.save(user_input, msg)
        return AgentResponse(message=msg, tools_used=["search_obsidian", "get_omi"], context={})