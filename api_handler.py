import requests

API_KEY = "your_api_key"
BASE_URL = "https://api.collegefootballdata.com"

def get_teams():
    response = requests.get(f"{BASE_URL}/teams/fbs", headers={"Authorization": f"Bearer {API_KEY}"})
    if response.status_code == 200:
        return [team["school"] for team in response.json()]
    else:
        return []