import json
from database import matches, games, players

# อ่าน JSON ไฟล์
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# ✅ Insert ข้อมูล Matches
match_data = load_json("app/data/matches.json")
matches.update_many(match_data)
print(f"✅ Inserted {len(match_data)} matches")

# ✅ Insert ข้อมูล Games
game_data = load_json("app/data/games.json")
games.update_many(game_data)
print(f"✅ Inserted {len(game_data)} games")

# ✅ Insert ข้อมูล Players
player_data = load_json("app/data/players.json")
players.update_many(player_data)
print(f"✅ Inserted {len(player_data)} players")
