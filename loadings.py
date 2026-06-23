import os, json, defaults, data

def load_all_challenges():
    os.makedirs('cache/challenges', exist_ok=True)
    if os.path.exists('cache/challenges/all_challenges.json'):
        with open('cache/challenges/all_challenges.json', 'r', encoding='utf-8') as f:
            data.all_challenges = json.load(f)
    else:
        defaults.all_challenges_default()
def load_challenges_data():
    os.makedirs("cache/challenges", exist_ok=True)
    if os.path.exists("cache/challenges/challenges_data.json"):
        with open("cache/challenges/challenges_data.json", "r", encoding='utf-8') as f:
            data.challenges_data = json.load(f)
    else:
        defaults.challengesdata_default()
def load_challenges_statuses():
    os.makedirs("cache/challenges", exist_ok=True)
    if os.path.exists("cache/challenges/challenges_status.json"):
        with open("cache/challenges/challenges_status.json", "r", encoding='utf-8') as f:
            data.challenges_statuses = json.load(f)
    else:
        defaults.challenges_statuses_default()
def load_challenges_list():
    os.makedirs("cache/challenges", exist_ok=True)
    if os.path.exists("cache/challenges/challenges_list.json"):
        with open("cache/challenges/challenges_list.json", "r", encoding='utf-8') as f:
            data.challenges_list = json.load(f)
    else:
        defaults.challenges_list_default()

def load_userdata():
    os.makedirs('cache', exist_ok=True)
    if os.path.exists("cache/userData.json"):
        with open('cache/userData.json', 'r', encoding='utf-8') as f:
            data.userdata = json.load(f)
    else:
        defaults.userdata_default()
def load_sysdata():
    os.makedirs('cache', exist_ok=True)
    if os.path.exists("cache/sysData.json"):
        with open('cache/sysData.json', 'r', encoding='utf-8') as f:
            data.sysdata = json.load(f)
    else:
        defaults.sysdata_default()

def load_task_statuses():
    os.makedirs('cache/tasks', exist_ok=True)
    if os.path.exists("cache/tasks/taskStatuses.json"):
        with open('cache/tasks/taskStatuses.json', 'r', encoding='utf-8') as f:
            data.task_statuses = json.load(f)
    else:
        defaults.task_status_default()
def load_taskdata():
    os.makedirs('cache/tasks', exist_ok=True)
    if os.path.exists("cache/tasks/taskData.json"):
        with open('cache/tasks/taskData.json', 'r', encoding='utf-8') as f:
            data.taskdata = json.load(f)
    else:
        defaults.taskdata_default()
def load_task_word_list():
    os.makedirs('cache/tasks', exist_ok=True)
    if os.path.exists("cache/tasks/tasksWordList.json"):
        with open('cache/tasks/tasksWordList.json', 'r', encoding='utf-8') as f:
            data.task_word_list = json.load(f)
    else:
        defaults.task_word_list_default()
def load_tasklist():
    os.makedirs('cache/tasks', exist_ok=True)
    if os.path.exists("cache/tasks/task_list.json"):
        with open('cache/tasks/task_list.json', 'r', encoding='utf-8') as f:
            data.tasklist = json.load(f)
    else:
        defaults.default_tasklist()
def load_bonus_userdata():
    os.makedirs('cache/bonuses', exist_ok=True)
    if os.path.exists("cache/bonuses/user_data.json"):
        with open('cache/bonuses/user_data.json', 'r', encoding='utf-8') as f:
            data.bonus_userdata = json.load(f)
    else:
        defaults.bonus_userdata_default()
def load_bonus_data():
    os.makedirs('cache/bonuses', exist_ok=True)
    if os.path.exists("cache/bonuses/bonus_data.json"):
        with open('cache/bonuses/bonus_data.json', 'r', encoding='utf-8') as f:
            data.bonusdata = json.load(f)
    else:
        defaults.bonus_data_default()
def load_bonus_list():
    os.makedirs('cache/bonuses', exist_ok=True)
    if os.path.exists("cache/bonuses/bonus_list.json"):
        with open('cache/bonuses/bonus_list.json', 'r', encoding='utf-8') as f:
            data.bonus_list = json.load(f)
    else:
        defaults.bonus_list_default()