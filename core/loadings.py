
# === IMPORTS ===
import os, json
from core import data

# === CLASSES ===
class CriticalFileError(Exception):
    pass
class UserFileError(Exception):
    pass

# === USERDATA LOADS ===
def load_user_quests():
    if os.path.exists(f'cache/userdata/quests.json'):
        with open(f'cache/userdata/quests.json', 'r', encoding='utf-8') as f:
            data.user_quests = json.load(f)
    else:
        raise UserFileError()
def load_user_profile():
    if os.path.exists(f'cache/userdata/profile.json'):
        with open(f'cache/userdata/profile.json', 'r', encoding='utf-8') as f:
            data.user_profile = json.load(f)
    else:
        raise UserFileError()
def load_user_logs():
    if os.path.exists(f'cache/userdata/logs.json'):
        with open(f'cache/userdata/logs.json', 'r', encoding='utf-8') as f:
            data.user_logs = json.load(f)
    else:
        raise UserFileError()
def load_user_config():
    if os.path.exists(f'cache/userdata/config.json'):
        with open(f'cache/userdata/config.json', 'r', encoding='utf-8') as f:
            data.user_config = json.load(f)
    else:
        raise UserFileError()
# === LANGUAGES LOADS ===
def load_lang_achievments():
    if os.path.exists(f'cache/languages/{data.user_config["language"]}/achievements.json'):
        with open(f'cache/languages/{data.user_config["language"]}/achievements.json', 'r', encoding='utf-8') as f:
            data.lang_achievements = json.load(f)
    else:
        raise CriticalFileError()
def load_lang_events():
    if os.path.exists(f'cache/languages/{data.user_config["language"]}/events.json'):
        with open(f'cache/languages/{data.user_config["language"]}/events.json', 'r', encoding='utf-8') as f:
            data.lang_events = json.load(f)
    else:
        raise CriticalFileError()
def load_lang_familiar():
    if os.path.exists(f'cache/languages/{data.user_config["language"]}/familiars.json'):
        with open(f'cache/languages/{data.user_config["language"]}/familiars.json', 'r', encoding='utf-8') as f:
            data.lang_familiars = json.load(f)
    else:
        raise CriticalFileError()
def load_lang_locations():
    if os.path.exists(f'cache/languages/{data.user_config["language"]}/locations.json'):
        with open(f'cache/languages/{data.user_config["language"]}/locations.json', 'r', encoding='utf-8') as f:
            data.lang_locations = json.load(f)
    else:
        raise CriticalFileError()
def load_lang_quest_givers():
    if os.path.exists(f'cache/languages/{data.user_config["language"]}/quest_givers.json'):
        with open(f'cache/languages/{data.user_config["language"]}/quest_givers.json', 'r', encoding='utf-8') as f:
            data.lang_quest_givers = json.load(f)
    else:
        raise CriticalFileError()
def load_lang_tutorial():
    if os.path.exists(f'cache/languages/{data.user_config["language"]}/tutorial.json'):
        with open(f'cache/languages/{data.user_config["language"]}/tutorial.json', 'r', encoding='utf-8') as f:
            data.lang_tutorial = json.load(f)
    else:
        raise CriticalFileError()
def load_lang_ui():
    if os.path.exists(f'cache/languages/{data.user_config["language"]}/ui.json'):
        with open(f'cache/languages/{data.user_config["language"]}/ui.json', 'r', encoding='utf-8') as f:
            data.lang_ui = json.load(f)
    else:
        raise CriticalFileError()

# === SYSDATA LOADS ===
def load_sys_achievments():
    if os.path.exists(f'cache/sysdata/achievements.json'):
        with open(f'cache/sysdata/achievements.json', 'r', encoding='utf-8') as f:
            data.sys_achievements = json.load(f)
    else:
        raise CriticalFileError()
def load_sys_events():
    if os.path.exists(f'cache/sysdata/events.json'):
        with open(f'cache/sysdata/events.json', 'r', encoding='utf-8') as f:
            data.sys_events = json.load(f)
    else:
        raise CriticalFileError()
def load_sys_familiar():
    if os.path.exists(f'cache/sysdata/familiar.json'):
        with open(f'cache/sysdata/familiar.json', 'r', encoding='utf-8') as f:
            data.sys_familiar = json.load(f)
    else:
        raise CriticalFileError()
def load_sys_locations():
    if os.path.exists(f'cache/sysdata/locations.json'):
        with open(f'cache/sysdata/locations.json', 'r', encoding='utf-8') as f:
            data.sys_locations = json.load(f)
    else:
        raise CriticalFileError()
def load_sys_quest_givers():
    if os.path.exists(f'cache/sysdata/quest_givers.json'):
        with open(f'cache/sysdata/quest_givers.json', 'r', encoding='utf-8') as f:
            data.sys_quest_givers = json.load(f)
    else:
        raise CriticalFileError()
def load_sys_task_pool():
    if os.path.exists(f'cache/sysdata/task_pool.json'):
        with open(f'cache/sysdata/task_pool.json', 'r', encoding='utf-8') as f:
            data.sys_task_pool = json.load(f)
    else:
        raise CriticalFileError()