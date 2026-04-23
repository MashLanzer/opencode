# home-assistant-integration.py
# OpenCode - Home Assistant Integration

import os
import requests
from datetime import datetime

# ============= CONFIGURATION =============
HOME_ASSISTANT_URL = os.getenv("HA_URL", "http://homeassistant.local:8123")
HA_TOKEN = os.getenv("HA_TOKEN", "")  # Get from Home Assistant

# ============= FUNCTIONS =============

def get_ha_headers():
    return {
        "Authorization": f"Bearer {HA_TOKEN}",
        "Content-Type": "application/json"
    }

def get_states():
    """Get all entity states"""
    response = requests.get(
        f"{HOME_ASSISTANT_URL}/api/states",
        headers=get_ha_headers(),
        timeout=10
    )
    if response.status_code == 200:
        return response.json()
    return []

def get_state(entity_id):
    """Get specific entity state"""
    response = requests.get(
        f"{HOME_ASSISTANT_URL}/api/states/{entity_id}",
        headers=get_ha_headers(),
        timeout=10
    )
    if response.status_code == 200:
        return response.json()
    return None

def call_service(domain, service, data=None):
    """Call a Home Assistant service"""
    response = requests.post(
        f"{HOME_ASSISTANT_URL}/api/services/{domain}/{service}",
        headers=get_ha_headers(),
        json=data or {},
        timeout=10
    )
    return response.status_code == 200

def notify_opencode_status(status):
    """Notify OpenCode status via HA"""
    message = f"OpenCode: {status}"
    return call_service("notify", "persistent_notification", {
        "message": message,
        "title": "OpenCode Assistant"
    })

def set_opencode_light(color="green"):
    """Set light based on OpenCode status"""
    color_map = {
        "green": [255, 182, 193],  # Active
        "yellow": [255, 255, 0],   # Waiting
        "red": [255, 0, 0],        # Issue
    }
    
    rgb = color_map.get(color, [255, 255, 255])
    
    # Assuming there's a light entity
    return call_service("light", "turn_on", {
        "entity_id": "light.opencode_status",
        "rgb_color": rgb
    })

def check_opencode_active():
    """Check if OpenCode was recently active"""
    # This would check for recent activity
    # For now, return True as placeholder
    return True

# ============= MAIN =============

def main():
    print("=== Home Assistant Integration ===")
    
    if not HA_TOKEN:
        print("WARNING: HA_TOKEN not set")
        print("Set with: export HA_TOKEN='your_token'")
        return
    
    print("\n1. Getting states...")
    states = get_states()
    print(f"   Total entities: {len(states)}")
    
    print("\n2. Testing service call...")
    # Test notification (commented out to avoid spam)
    # notify_opencode_status("OpenCode connected!")
    
    print("\n=== Ready ===")

if __name__ == "__main__":
    main()