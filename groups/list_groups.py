import requests
from auth.graph_auth import get_graph_token
from utils.csv_writer import write_csv

GRAPH_URL = "https://graph.microsoft.com/v1.0/groups"

def list_groups():
    token = get_graph_token()
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(GRAPH_URL, headers=headers)
    response.raise_for_status()

    groups = response.json().get("value", [])
    write_csv("groups.csv", groups)

    print(f"Exported {len(groups)} groups to groups.csv")

if __name__ == "__main__":
    list_groups()
