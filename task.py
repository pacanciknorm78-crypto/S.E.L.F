import gui, data, random

def task_completing():
    gui.task_diff_choice()
    diff = input("... --> ").lower()
    difficulties = ["c", "b", "a", "s", "ss"]
    if diff in difficulties:
        gui.task_num_choice()
        num = int(input("... --> "))
        data.task_statuses[f"{diff}"][f"is{num}TaskComplete"] = True

def task_reroll():
    gui.tasksreroll()
    task_generator()

def task_generator():
    wordlist = data.task_word_list
    categorys = wordlist["categorys"]
    weights = wordlist["weights"]
    for diff in ["C", "B", "A", "S", "SS"]:
        amount = data.taskdata[f"amountQuests_{diff}_tier"]
        for i in range(amount):
            task_category = random.choices(categorys, weights[diff], k=1)[0]
            task = f"{diff} {random.choice(wordlist["action_category"][f"{task_category}"])} {random.choice(wordlist["objects_by_category"][f"{task_category}"])}"
            data.tasklist[f"{diff.lower()}"][i] = task
