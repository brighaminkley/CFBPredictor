import os
import json
import requests

API_KEY = "ocJb8eqMbcVGwrupKsY7/9v8FJv+ecBXcsvOfGWfMK7PSFIfEd/t3KCHUr3ew9ki"
BASE_URL = "https://api.collegefootballdata.com"
CACHE_FILE = "teams.json"

def get_teams():
    # Step 1: Use cache if available
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, "r") as f:
            return json.load(f)

    # Step 2: Otherwise, fetch from API
    url = f"{BASE_URL}/teams/fbs"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        teams_data = response.json()
        teams = sorted([team["school"] for team in teams_data])
        
        # Save to cache
        with open(CACHE_FILE, "w") as f:
            json.dump(teams, f)

        return teams
    else:
        print("Failed to fetch teams:", response.status_code)
        return []