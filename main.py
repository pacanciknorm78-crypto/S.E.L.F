import loadings, saves, data

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

def main():
        on_start()
        print(data.tasklist)

if __name__ == '__main__':
        main()