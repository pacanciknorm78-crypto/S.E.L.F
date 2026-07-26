import json
from gui.gui import contact_information

def recovery():
    default_user_config()
    default_user_logs()
    default_user_profile()
    default_user_quests()
    contact_information()

def default_user_config():
    default_data = {}
    with open('cache/userdata/config.json', 'w', encoding='utf-8') as f:
        json.dump(default_data, f, ensure_ascii=False, indent=2)
def default_user_logs():
    default_data = {}
    with open('cache/userdata/logs.json', 'w', encoding='utf-8') as f:
        json.dump(default_data, f, ensure_ascii=False, indent=2)
def default_user_profile():
    default_data = {}
    with open('cache/userdata/profile.json', 'w', encoding='utf-8') as f:
        json.dump(default_data, f, ensure_ascii=False, indent=2)
def default_user_quests():
    default_data = {}
    with open('cache/userdata/quests.json', 'w', encoding='utf-8') as f:
        json.dump(default_data, f, ensure_ascii=False, indent=2)