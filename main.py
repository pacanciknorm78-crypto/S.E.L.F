import loadings, saves, gui, task, data
import challenge, bonus

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
    loadings.load_bonus_data()
    loadings.load_bonus_list()
    loadings.load_bonus_userdata()
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
        "0": campfire
    }
    gui.tasks()
    userinput = input("... --> ")
    if userinput in choices:
        action = choices.get(userinput)
        action()
def challenges():
    choises = {
        "1": challenge.challenges_completing,
        "2": campfire,
        #"debugreroll": challenge.challenges,
    }
    gui.challenges()
    userinput = input("... --> ")
    if userinput in choises:
        action = choises.get(userinput)
        action()
def bonuses():
    choices = {
        "1": bonus.shop,
        "2": bonus.burmalda,
        "3": bonus.description,
        "0": campfire
    }
    gui.bonuses()
    userinput = input("... --> ")
    if userinput in choices:
        action = choices.get(userinput)
        action()
def stats():
    choices = {}
def familyar():
    choices = {}
def inventory():
    choices = {}
def world_map():
    choices = {}
def menu():
    choices = {}
def campfire():
    choices = {
        "1": stats,
        "2": familyar,
        "3": tasks,
        "4": inventory,
        "5": world_map,
        "menu": menu
    }
    gui.campfire()
    userinput = input("... --> ")
    if userinput in choices:
            action = choices.get(userinput)
            action()


def main():
    on_start()
    while True:
        if data.userdata["needWelcomeScreen"]:
            gui.welcome_screen()
            data.userdata["needWelcomeScreen"] = False
            saves.save_userdata()
        else:
            campfire()
    # if data.tasklist["c"][0] == "1":
    #     task.task_generator()
    # else:
    #     while True:
    #         #bonus.bonus_add()
    #         menu()


if __name__ == '__main__':
    main()