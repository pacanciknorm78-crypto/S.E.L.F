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
    gui.bill_board()
    userinput = input("... --> ")
    if userinput in choices:
        action = choices.get(userinput)
        action()

def stats():
    choices = {"1": campfire,
               "2": characteristics}
    gui.stats()
    userinput = input("... --> ")
    if userinput in choices:
        action = choices.get(userinput)
        action()
    else:
        gui.invalid_input()
        stats()
def characteristics():
    choices = {"1": campfire,
               "2": stats}
    gui.characteristics()
    userinput = input("... --> ")
    if userinput in choices:
        action = choices.get(userinput)
        action()
    else:
        gui.invalid_input()
        characteristics()

def familyar():
    choices = {}
    gui.familyar()
    userinput = input("... --> ")
    if userinput in choices:
        action = choices.get(userinput)
        action()
    else:
        gui.invalid_input()
        familyar()
def inventory():
    choices = {}
    gui.equipment()
    userinput = input("... --> ")
    if userinput in choices:
        action = choices.get(userinput)
        action()
    else:
        gui.invalid_input()
        inventory()
def world_map():
    choices = {}
    gui.world_map()
    userinput = input("... --> ")
    if userinput in choices:
        action = choices.get(userinput)
        action()
    else:
        gui.invalid_input()
        world_map()
def menu():
    choices = {}
    gui.campfire()
    userinput = input("... --> ")
    if userinput in choices:
        action = choices.get(userinput)
        action()
    else:
        gui.invalid_input()
        campfire()
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
    else:
        gui.invalid_input()
        campfire()

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
"""
TODO
заглушки + основные меню
внешние модули
кор + логика
"""