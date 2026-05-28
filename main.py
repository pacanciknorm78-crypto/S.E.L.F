import loadings, saves, gui

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
    gui.tasks()
def challenges():
    gui.challenges()
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
    while True:
        menu()


if __name__ == '__main__':
    main()