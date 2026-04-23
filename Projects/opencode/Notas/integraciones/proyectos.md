# Linear / Notion - Project Management

## Linear
- API: GraphQL
- Para equipos

## Notion
- API: REST
- Bases de datos

## Uso
```python
# Linear
from linear_notion_integration import create_linear_issue
create_linear_issue("Nueva tarea", "Descripcion")

# Notion  
create_notion_page(database_id, "Titulo")
```

## Variables
- LINEAR_API_KEY
- NOTION_API_KEY