# gmail-integration.py
# OpenCode Gmail Integration

import os
import base64
import json
from typing import Optional, List
from datetime import datetime

import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.message import EmailMessage

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
    "https://www.googleapis.com/auth/gmail.modify"
]

CREDS_PATH = os.getenv("CREDS_PATH", "credentials.json")
TOKEN_PATH = os.getenv("TOKEN_PATH", "token.json")

OBSIDIAN_URL = "http://127.0.0.1:27123"
OBSIDIAN_API_KEY = os.getenv("OBSIDIAN_API_KEY", "dadde3d8184f6aae78239eb4570ac4430b55532fcf5afb77fd081f70c7e0c459")

def get_credentials():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_info(json.load(open(TOKEN_PATH)), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(request=None)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
            creds = flow.run_local_server(port=8080)
        with open(TOKEN_PATH, "w") as f:
            f.write(creds.to_json())
    return creds

def get_gmail_service():
    return build("gmail", "v1", credentials=get_credentials())

def create_message(to: str, subject: str, body: str) -> dict:
    msg = EmailMessage()
    msg.set_content(body)
    msg["To"], msg["From"], msg["Subject"] = to, "me", subject
    return {"raw": base64.urlsafe_b64encode(msg.as_bytes()).decode()}

class GmailClient:
    def __init__(self):
        self.service = None
    
    def initialize(self):
        if not self.service:
            try:
                self.service = get_gmail_service()
            except Exception as e:
                print(f"Gmail init error: {e}")
    
    def send_email(self, to: str, subject: str, body: str) -> Optional[str]:
        self.initialize()
        if not self.service:
            return None
        try:
            msg = create_message(to, subject, body)
            sent = self.service.users().messages().send(userId="me", body=msg).execute()
            return sent.get("id")
        except HttpError as e:
            print(f"Error: {e}")
            return None
    
    def get_emails(self, query: str = "", limit: int = 10) -> List[dict]:
        self.initialize()
        if not self.service:
            return []
        try:
            results = self.service.users().messages().list(userId="me", q=query, maxResults=limit).execute()
            return [self.service.users().messages().get(userId="me", id=m["id"]).execute() 
                    for m in results.get("messages", [])]
        except:
            return []

def send_daily_brief(recipient: str) -> bool:
    client = GmailClient()
    headers = {"Authorization": f"Bearer {OBSIDIAN_API_KEY}"}
    content = "# Daily Brief\n"
    try:
        r = requests.get(f"{OBSIDIAN_URL}/vault/Notas/tareas/pendientes.md", headers=headers)
        if r.status_code == 200:
            content += r.text[:500]
    except:
        pass
    return client.send_email(recipient, f"Daily Brief - {datetime.now().strftime('%Y-%m-%d')}", content) is not None

def main():
    print("📧 Gmail Test")
    client = GmailClient()
    result = client.send_email("brayanibarra0105@gmail.com", "Test", "OpenCode Test")
    print(f"{'✅' if result else '❌'} - Set credentials.json")

if __name__ == "__main__":
    main()