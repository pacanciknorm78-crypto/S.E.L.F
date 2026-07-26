from core.loadings import CriticalFileError, UserFileError
from gui import gui
from core import loadings, saves, task, data, defaults
import sys
def on_start():
    try:
        loadings.load_user_config()
        loadings.load_user_logs()
        loadings.load_user_profile()
        loadings.load_user_quests()
    except UserFileError:
        choices = {
            "save-exit": sys.exit,
            "recovery": defaults.recovery
        }
        gui.user_packet_loading_error()
        userinput = input("... --> ")
        if userinput in choices:
            action = choices.get(userinput)
            action()
    try:
        loadings.load_lang_achievments()
        loadings.load_lang_events()
        loadings.load_lang_familiar()
        loadings.load_lang_locations()
        loadings.load_lang_quest_givers()
        loadings.load_lang_tutorial()
        loadings.load_lang_ui()
        loadings.load_sys_achievments()
        loadings.load_sys_events()
        loadings.load_sys_familiar()
        loadings.load_sys_locations()
        loadings.load_sys_quest_givers()
        loadings.load_sys_task_pool()
    except (CriticalFileError, KeyError):
        gui.critical_packet_loading_error()
        sys.exit(1)
def on_exit():
    saves.save_user_config()
    saves.save_user_logs()
    saves.save_user_profile()
    saves.save_user_quests()
def tasks():
    choices = {
        # "1": task.task_completing,
        # "2": task.task_reroll,
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
    while True: campfire()
        # if data.userdata["needWelcomeScreen"]:
        #     gui.welcome_screen()
        #     data.userdata["needWelcomeScreen"] = False
        #     saves.save_userdata()
        # else:
        #     campfire()
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