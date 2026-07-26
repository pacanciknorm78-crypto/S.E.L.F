import json
from core import data

def save_user_config():
    with open('cache/userdata/config.json', 'w', encoding='utf-8') as f:
        json.dump(data.user_config, f, ensure_ascii=False, indent=2)
def save_user_logs():
    with open('cache/userdata/logs.json', 'w', encoding='utf-8') as f:
        json.dump(data.user_logs, f, ensure_ascii=False, indent=2)
def save_user_quests():
    with open('cache/userdata/quests.json', 'w', encoding='utf-8') as f:
        json.dump(data.user_quests, f, ensure_ascii=False, indent=2)
def save_user_profile():
    with open('cache/userdata/profile.json', 'w', encoding='utf-8') as f:
        json.dump(data.user_profile, f, ensure_ascii=False, indent=2)