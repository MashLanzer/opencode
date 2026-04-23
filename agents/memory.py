# agents/memory.py
import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Optional
from pathlib import Path

DB_PATH = Path(__file__).parent / "agent_memory.db"

class AgentMemory:
    def __init__(self, db_path: str = None):
        self.db_path = db_path or str(DB_PATH)
        self._init()
    
    def _init(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY, agent TEXT, user_message TEXT, assistant_message TEXT,
            context TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
        c.execute("""CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY, agent TEXT, key TEXT, value TEXT,
            metadata TEXT, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
        conn.commit()
        conn.close()
    
    def add_conversation(self, agent: str, user_msg: str, assistant_msg: str, context: Dict):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("""INSERT INTO conversations (agent, user_message, assistant_message, context) 
            VALUES (?, ?, ?, ?)""", (agent, user_msg, assistant_msg, json.dumps(context)))
        conn.commit()
        conn.close()
    
    def get_context(self, agent: str, limit: int = 5) -> List[Dict]:
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("""SELECT user_message, assistant_message, context FROM conversations 
            WHERE agent = ? ORDER BY created_at DESC LIMIT ?""", (agent, limit))
        results = [{"user": r[0], "assistant": r[1], "context": json.loads(r[2]) if r[2] else {}} 
                  for r in c.fetchall()]
        conn.close()
        return results
    
    def set_memory(self, agent: str, key: str, value: str):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("""INSERT OR REPLACE INTO memories (agent, key, value, updated_at) 
            VALUES (?, ?, ?, ?)""", (agent, key, value, datetime.now().isoformat()))
        conn.commit()
        conn.close()
    
    def get_memory(self, agent: str, key: str) -> Optional[str]:
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute("SELECT value FROM memories WHERE agent = ? AND key = ?", (agent, key))
        r = c.fetchone()
        conn.close()
        return r[0] if r else None