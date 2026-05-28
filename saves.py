import json, data

def save_userdata():
    with open('cache/userData.json', 'w', encoding='utf-8') as f:
        json.dump(data.userdata, f, ensure_ascii=False, indent=4)
def save_task_statuses():
    with open('cache/tasks/taskStatuses.json', 'w', encoding='utf-8') as f:
        json.dump(data.task_statuses, f, ensure_ascii=False, indent=2)
def save_tasklist():
    with open('cache/tasks/task_list.json', 'w', encoding='utf-8') as f:
        json.dump(data.tasklist, f, ensure_ascii=False, indent=4)
def save_challenges_list():
    with open('cache/tasks/taskChallenges.json', 'w', encoding='utf-8') as f:
        json.dump(data.challenges_list, f, ensure_ascii=False, indent=2)
def save_challenges_status():
    with open('cache/tasks/taskChallengeStatus.json', 'w', encoding='utf-8') as f:
        json.dump(data.challenges_statuses, f, ensure_ascii=False, indent=2)
def save_challenges_data():
    with open('cache/challenges/challenges_data.json', 'w', encoding='utf-8') as f:
        json.dump(data.challenges_data, f, ensure_ascii=False, indent=2)