# linear-notion-integration.py
# OpenCode - Linear / Notion Integration for Project Management

import os
import requests
from datetime import datetime

# ============= LINEAR CONFIG =============
LINEAR_API_KEY = os.getenv("LINEAR_API_KEY", "")
LINEAR_API_URL = "https://api.linear.app/graphql"

# ============= NOTION CONFIG =============
NOTION_API_KEY = os.getenv("NOTION_API_KEY", "")
NOTION_API_URL = "https://api.notion.com/v1"

# ============= LINEAR FUNCTIONS =============

def linear_query(query, variables=None):
    """Make GraphQL request to Linear"""
    if not LINEAR_API_KEY:
        return {"error": "No LINEAR_API_KEY set"}
    
    headers = {
        "Authorization": LINEAR_API_KEY,
        "Content-Type": "application/json"
    }
    
    data = {"query": query}
    if variables:
        data["variables"] = variables
    
    try:
        response = requests.post(
            LINEAR_API_URL,
            headers=headers,
            json=data,
            timeout=10
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def get_linear_issues():
    """Get all issues"""
    query = """
    query {
        issues(first: 20) {
            nodes {
                id
                title
                state {
                    name
                }
                priority
                createdAt
            }
        }
    }
    """
    return linear_query(query)

def create_linear_issue(title, description="", team_id=None):
    """Create a new issue"""
    mutation = """
    mutation CreateIssue($input: IssueCreateInput!) {
        issueCreate(input: $input) {
            success
            issue {
                id
                title
            }
        }
    }
    """
    variables = {
        "input": {
            "title": title,
            "description": description
        }
    }
    return linear_query(mutation, variables)

# ============= NOTION FUNCTIONS =============

def get_notion_headers():
    return {
        "Authorization": f"Bearer {NOTION_API_KEY}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28"
    }

def query_notion_database(database_id):
    """Query a Notion database"""
    if not NOTION_API_KEY:
        return {"error": "No NOTION_API_KEY set"}
    
    try:
        response = requests.post(
            f"{NOTION_API_URL}/databases/{database_id}/query",
            headers=get_notion_headers(),
            json={"page_size": 25},
            timeout=10
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}

def create_notion_page(database_id, title, properties=None):
    """Create a new page in Notion"""
    if not NOTION_API_KEY:
        return {"error": "No NOTION_API_KEY set"}
    
    data = {
        "parent": {"database_id": database_id},
        "properties": {
            "Name": {
                "title": [{"text": {"content": title}}]
            }
        }
    }
    
    if properties:
        data["properties"].update(properties)
    
    try:
        response = requests.post(
            f"{NOTION_API_URL}/pages",
            headers=get_notion_headers(),
            json=data,
            timeout=10
        )
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# ============= MAIN =============

def main():
    print("=== Linear / Notion Integration ===")
    
    # Linear test
    if LINEAR_API_KEY:
        print("\n1. Testing Linear...")
        result = get_linear_issues()
        print(f"   Issues: {len(result.get('data', {}).get('issues', {}).get('nodes', []))}")
    else:
        print("\n1. Linear: No API key (set LINEAR_API_KEY)")
    
    # Notion test
    if NOTION_API_KEY:
        print("\n2. Testing Notion...")
        print("   Ready for database queries")
    else:
        print("\n2. Notion: No API key (set NOTION_API_KEY)")
    
    print("\n=== Ready ===")

if __name__ == "__main__":
    main()