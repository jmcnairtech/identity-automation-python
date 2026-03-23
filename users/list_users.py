import requests
from auth.graph_auth import get_graph_token
from utils.csv_writer import write_csv

GRAPH_URL = "https://graph.microsoft.com/v1.0/users"

def list_users():
    token = get_graph_token()
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(GRAPH_URL, headers=headers)
    response.raise_for_status()

    users = response.json().get("value", [])
    write_csv("users.csv", users)

    print(f"Exported {len(users)} users to users.csv")

if __name__ == "__main__":
    list_users()
