# anki-integration.py
# OpenCode - Anki Spaced Repetition Integration

import os
import requests
import json
from datetime import datetime

# ============= CONFIGURATION =============
ANKI_CONNECT_URL = os.getenv("ANKI_URL", "http://localhost:8765")
ANKI_API_KEY = os.getenv("ANKI_API_KEY", "")

# ============= FUNCTIONS =============

def anki_request(action, params=None):
    """Make request to AnkiConnect"""
    data = {
        "action": action,
        "version": 6
    }
    if params:
        data["params"] = params
    
    try:
        response = requests.post(
            ANKI_CONNECT_URL,
            json=data,
            timeout=10
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_deck_names():
    """Get all deck names"""
    result = anki_request("getDeckNames")
    return result.get("result", [])

def create_deck(deck_name):
    """Create a new deck"""
    return anki_request("createDeck", {"deck": deck_name})

def add_note(deck_name, front, back, tags=""):
    """Add a flashcard to a deck"""
    params = {
        "note": {
            "deckName": deck_name,
            "modelName": "Basic",
            "fields": {
                "Front": front,
                "Back": back
            },
            "tags": tags.split(",") if tags else []
        }
    }
    return anki_request("addNote", params)

def find_notes(query):
    """Find notes matching query"""
    return anki_request("findNotes", {"query": query})

def add_notes_from_text(text, deck_name="OpenCode", tags="opencode"):
    """Automatically create cards from text"""
    cards = []
    
    # Split by lines or sentences
    lines = text.split("\n")
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        # Simple Q/A detection
        if " - " in line:
            parts = line.split(" - ", 1)
            front = parts[0].strip()
            back = parts[1].strip() if len(parts) > 1 else ""
        elif ":" in line:
            parts = line.split(":", 1)
            front = parts[0].strip()
            back = parts[1].strip() if len(parts) > 1 else ""
        else:
            front = line
            back = "Definir respuesta"
        
        result = add_note(deck_name, front, back, tags)
        if result.get("error"):
            print(f"Error: {result[error]}")
        else:
            cards.append(front)
    
    return cards

def export_from_obsidian_tag(tag="aprender"):
    """Export notes with specific tag to Anki"""
    # This would integrate with Obsidian
    # For now, returns placeholder
    return {
        "status": "ready",
        "tag": tag,
        "message": "Use add_notes_from_text() to create cards"
    }

# ============= MAIN =============

def main():
    print("=== Anki Integration ===")
    
    print("\n1. Testing connection...")
    result = anki_request("ping")
    print(f"   Ping: {result}")
    
    print("\n2. Getting decks...")
    decks = get_deck_names()
    print(f"   Decks: {decks[:5]}..." if len(decks) > 5 else f"   Decks: {decks}")
    
    print("\n3. Testing card creation...")
    test_card = add_note("OpenCode", "Test", "This is a test card", "test")
    print(f"   Result: {test_card}")
    
    print("\n=== Ready ===")

if __name__ == "__main__":
    main()