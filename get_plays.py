import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

CFBD_API_KEY = os.environ.get("CFBD_API_KEY")

base_url = "https://api.collegefootballdata.com/plays"
headers = {"Authorization": f"Bearer {CFBD_API_KEY}"}

seasons = [2019, 2020, 2021, 2022, 2023]
weeks = range(1, 16)

play_by_play = []

for season in seasons:
    for week in weeks:
        params = {
            "year": season,
            "week": week
        }
        response = requests.get(base_url, params=params, headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            play_by_play.extend(data)
        elif response.status_code == 429:
            print(f"Rate limit exceeded for season {season}, week {week}. Retrying...")
        else:
            print(f"Error: {response.status_code} for season {season}, week {week}")

plays_df = pd.DataFrame(play_by_play)
plays_df.to_csv("play_by_play_2019-2023.csv", index=False)
