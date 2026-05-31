import random, data, saves, gui
def challenges():
    chal_list = data.challenges_list
    all_chal_list = data.all_challenges
    chal_stat = data.challenges_statuses
    for diff in ["easy", "normal", "hard", "insane", "demonic"]:
        for i in range(2):
            challenge = f"{random.choice(all_chal_list["all_challenges"][f"{diff}"])}"
            chal_list[f"{diff}"][i] = challenge
            chal_stat[f"{diff}"][f"is{i}Complete"] = False
    saves.save_challenges_list()
    saves.save_challenges_status()
def challenges_completing():
    gui.chall_diff()
    diff = input("... --> ").lower()
    if diff in ["easy", "normal", "hard", "insane", "demonic"]:
        gui.chall_num()
        num = int(input("... --> "))
        data.challenges_statuses[f"{diff}"][f"is{num-1}Complete"] = True
        saves.save_challenges_status()