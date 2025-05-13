import requests

API_KEY = "ocJb8eqMbcVGwrupKsY7/9v8FJv+ecBXcsvOfGWfMK7PSFIfEd/t3KCHUr3ew9ki"
BASE_URL = "https://api.collegefootballdata.com"

def get_teams():
    response = requests.get(f"{BASE_URL}/teams/fbs", headers={"Authorization": f"Bearer {API_KEY}"})
    if response.status_code == 200:
        return [team["school"] for team in response.json()]
    else:
        return []