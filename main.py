import loadings, saves, gui, task, data
import challenge

def on_start():
    loadings.load_userdata()
    loadings.load_sysdata()
    loadings.load_task_word_list()
    loadings.load_taskdata()
    loadings.load_tasklist()
    loadings.load_task_statuses()
    loadings.load_challenges_statuses()
    loadings.load_challenges_data()
    loadings.load_challenges_list()
    loadings.load_all_challenges()
def on_exit():
    saves.save_userdata()
    saves.save_task_statuses()
    saves.save_tasklist()
    saves.save_challenges_data()
    saves.save_challenges_list()
    saves.save_challenges_status()

def tasks():
    choices = {
        "1": task.task_completing,
        "2": task.task_reroll,
        "0": menu
    }
    gui.tasks()
    userinput = input("... --> ")
    if userinput in choices:
        action = choices.get(userinput)
        action()

def challenges():
    choises = {
        "1": challenge.challenges_completing,
        "2": menu,
        "debugreroll": challenge.challenges,
    }
    gui.challenges()
    userinput = input("... --> ")
    if userinput in choises:
        action = choises.get(userinput)
        action()

def bonuses():
    gui.bonuses()
def menu():
    choices = {
        "1": tasks,
        "2": challenges,
        "3": bonuses,
        "0": gui.menu,
        "9": gui.more
    }
    gui.menu()
    userinput = input("... --> ")
    if userinput in choices:
            action = choices.get(userinput)
            action()


def main():
    on_start()
    if data.tasklist["c"][0] == "1":
        task.task_generator()
    else:
        while True:
            menu()


if __name__ == '__main__':
    main()