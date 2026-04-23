---
tags: [integración, gmail]
creado: 2026-04-22
---

# 📧 Gmail Integration

| Función | Estado |
|---------|--------|
| send_email | ✅ Listo |
| get_emails | ✅ Listo |
| OAuth2 | ⚠️ Setup |

## Setup OAuth2
1. Google Cloud Console → APIs → Gmail API
2. Credentials → OAuth2 Client ID
3. Descargar credentials.json

## Uso
```python
from gmail_integration import GmailClient
client = GmailClient()
client.send_email("to@email.com", "Subject", "Body")
```

*Updated: 2026-04-22*