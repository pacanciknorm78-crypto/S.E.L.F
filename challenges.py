import random, data
def challenges():
    chal_list = data.challenges_list
    all_chal_list = data.all_challenges
    for diff in ["easy", "normal", "hard", "insane", "demonic"]:
        for i in range(2):
            challenge = f"{random.choice(all_chal_list[f"{diff}"])}"
            chal_list[f"{diff}"][i] = challenge
