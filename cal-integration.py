# calendar-integration.py
# OpenCode Cal.com Integration

import os
import requests
from datetime import datetime, timedelta

# ============= CONFIGURATION =============
CAL_API_KEY = os.getenv("CAL_API_KEY", "cal_live_9643088a06b3a5a774337b5e40485f93")
CAL_API_VERSION = "2024-08-13"
CAL_BASE_URL = "https://api.cal.com/v2"

# ============= HEADERS =============
def get_headers():
    return {
        "Authorization": f"Bearer {CAL_API_KEY}",
        "cal-api-version": CAL_API_VERSION,
        "Content-Type": "application/json"
    }

# ============= FUNCTIONS =============

def get_calendars():
    """Get all connected calendars"""
    response = requests.get(
        f"{CAL_BASE_URL}/calendars",
        headers=get_headers(),
        timeout=10
    )
    if response.status_code == 200:
        return response.json()
    return {"calendars": []}

def get_bookings(start_date=None, end_date=None):
    """Get upcoming bookings"""
    params = {}
    if start_date:
        params["startDate"] = start_date
    if end_date:
        params["endDate"] = end_date
    
    response = requests.get(
        f"{CAL_BASE_URL}/bookings",
        headers=get_headers(),
        params=params,
        timeout=10
    )
    if response.status_code == 200:
        return response.json()
    return {"bookings": []}

def get_event_types():
    """Get event types"""
    response = requests.get(
        f"{CAL_BASE_URL}/event-types",
        headers=get_headers(),
        timeout=10
    )
    if response.status_code == 200:
        return response.json()
    return {"eventTypes": []}

def create_booking(event_type_id, start_time, attendee_email, attendee_name):
    """Create a new booking"""
    data = {
        "eventTypeId": event_type_id,
        "start": start_time,  # ISO 8601 format
        "attendees": [
            {
                "email": attendee_email,
                "name": attendee_name
            }
        ]
    }
    
    response = requests.post(
        f"{CAL_BASE_URL}/bookings",
        headers=get_headers(),
        json=data,
        timeout=10
    )
    if response.status_code == 200:
        return response.json()
    return {"error": response.text}

def get_available_slots(date, event_type_id=None):
    """Get available time slots"""
    params = {"startTime": date}
    if event_type_id:
        params["eventTypeId"] = event_type_id
    
    response = requests.get(
        f"{CAL_BASE_URL}/slots",
        headers=get_headers(),
        params=params,
        timeout=10
    )
    if response.status_code == 200:
        return response.json()
    return {"slots": []}

def check_today_meetings():
    """Check meetings for today"""
    today = datetime.now().strftime("%Y-%m-%d")
    tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
    
    bookings = get_bookings(start_date=today, end_date=tomorrow)
    return bookings.get("bookings", [])

def prepare_meeting_context(booking):
    """Prepare context from a meeting"""
    context = {
        "title": booking.get("title", ""),
        "start_time": booking.get("startTime", ""),
        "end_time": booking.get("endTime", ""),
        "location": booking.get("location", ""),
        "description": booking.get("description", ""),
    }
    return context

# ============= MAIN TEST =============
def main():
    print("=== Cal.com Integration Test ===")
    
    # Test get calendars
    print("\n1. Getting calendars...")
    calendars = get_calendars()
    print(f"   Calendars: {len(calendars.get('calendars', []))}")
    
    # Test get event types
    print("\n2. Getting event types...")
    events = get_event_types()
    print(f"   Event types: {len(events.get('eventType', []))}")
    
    # Test get today's meetings
    print("\n3. Getting today's meetings...")
    meetings = check_today_meetings()
    print(f"   Meetings today: {len(meetings)}")
    
    print("\n=== Test Complete ===")

if __name__ == "__main__":
    main()