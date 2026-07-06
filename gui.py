import os, data
"""   operators && classes   """
class Sizes:
    header = 100
#print(f"║{"":^{Sizes.header}}║")
head     = "╔════════════════════════════════════════════════════════════════════════════════════════════════════╗"
ac       = f"║{"SelfControlling App by Takimka.(in develop)":^{Sizes.header}}║"
division = "╠════════════════════════════════════════════════════════════════════════════════════════════════════╣"
end      = "╚════════════════════════════════════════════════════════════════════════════════════════════════════╝"

def tasks():
    clear()
    print(head)
    print(f"║{"SelfControlling App by Takimka":^{Sizes.header}}║")
    print(division)
    print(f"╟{" Ежедневные Задания ":─^{Sizes.header}}╢")
    print(f"║{"":^{Sizes.header}}║")
    print(f"║{"  ==-->  Сложность класса С:   ":─<{Sizes.header-3}}   ║")
    for i in range(len(data.tasklist["c"])):
        text = data.tasklist["c"][i]
        num = f'{i+1}.'
        points = 10
        status = task_status_feedback("c", i+1)
        print(f"║ {num:<{3}} {crop_text(text, 62):<{62}} {points:>{6}}          {status:<{15}} ║")
    print(f"║{"  ==-->  Сложность класса В:   ":─<{Sizes.header - 3}}   ║")
    for i in range(len(data.tasklist["b"])):
        text = data.tasklist["b"][i]
        num = f'{i+1}.'
        points = 20
        status = task_status_feedback("b", i+1)
        print(f"║ {num:<{3}} {crop_text(text, 62):<{62}} {points:>{6}}          {status:<{15}} ║")
    print(f"║{"  ==-->  Сложность класса A:   ":─<{Sizes.header - 3}}   ║")
    for i in range(len(data.tasklist["a"])):
        text = data.tasklist["a"][i]
        num = f'{i + 1}.'
        points = 50
        status = task_status_feedback("a", i+1)
        print(f"║ {num:<{3}} {crop_text(text, 62):<{62}} {points:>{6}}          {status:<{15}} ║")
    print(f"║{"  ==-->  Сложность класса S:   ":─<{Sizes.header - 3}}   ║")
    for i in range(len(data.tasklist["s"])):
        text = data.tasklist["s"][i]
        num = f'{i + 1}.'
        points = 100
        status = task_status_feedback("s", i+1)
        print(f"║ {num:<{3}} {crop_text(text, 62):<{62}} {points:>{6}}          {status:<{15}} ║")
    print(f"║{"  ==-->  Сложность класса SS:   ":─<{Sizes.header - 3}}   ║")
    for i in range(len(data.tasklist["ss"])):
        text = data.tasklist["ss"][i]
        num = f'{i + 1}.'
        points = 150
        status = task_status_feedback("ss", i+1)
        print(f"║ {num:<{3}} {crop_text(text, 62):<{62}} {points:>{6}}          {status:<{15}} ║")
    print(f"╟{"":─^{Sizes.header}}╢")
    print(f"║{"1 - Отметить задание выполненым. 2 - 'Реролл'. 0 - Главное меню.":^{Sizes.header}}║")
    print(end)
def task_diff_choice():
    clear()
    print(head)
    print(f"║{"SelfControlling App by Takimka":^{Sizes.header}}║")
    print(division)
    print(f"╟{" Ежедневные Задания ":─^{Sizes.header}}╢")
    print(f"║{"":^{Sizes.header}}║")
    print(f"║{" Сейчас напиши сложность задания, которое выполнил.":^{Sizes.header}}║")
    print(f"║{" Следи за раскладкой своей клавиатуры, распознается только английский.":^{Sizes.header}}║")
    print(f"║{" Сложности: C, B, A, S, SS. Размер буквы не важен.":^{Sizes.header}}║")
    print(end)
def task_num_choice():
    clear()
    print(head)
    print(f"║{"SelfControlling App by Takimka":^{Sizes.header}}║")
    print(division)
    print(f"╟{" Ежедневные Задания ":─^{Sizes.header}}╢")
    print(f"║{"":^{Sizes.header}}║")
    print(f"║{" Сейчас напиши только номер задания, которое выполнил.":^{Sizes.header}}║")
    print(f"║{" Следи за раскладкой своей клавиатуры, распознается только английский.":^{Sizes.header}}║")
    print(f"║{" Номера для C: 1-10, B: 1-5, A: 1-4, S: 1-4, SS: 1-3. Размер буквы не важен.":^{Sizes.header}}║")
    print(end)
def tasksreroll():
    clear()
    print(head)
    print(f"║{"SelfControlling App by Takimka":^{Sizes.header}}║")
    print(division)
    print(f"╟{" Ежедневные Задания ":─^{Sizes.header}}╢")
    print(f"║{"":^{Sizes.header}}║")
    print(f"║{" Все задания сброшены, прогресс утерян":^{Sizes.header}}║")
    print(end)

def challenges():
    clear()
    print(head)
    print(ac)
    print(division)
    print(f"╟{" Еженедельные Испытания ":─^{Sizes.header}}╢")
    print(f"║{"":^{Sizes.header}}║")
    print(f"║{"  ==---> Легкие испытания:    ":─<{Sizes.header}}║")
    for i in range(len(data.challenges_list["easy"])):
        print(f"║ {i+1:<{1}}. {challenge_status_feedback("easy", i)}  {crop_text(data.challenges_list["easy"][i], 80):<{82}}  {data.challenges_data["sysData"]["amountPointForEasy"]:<{3}} {data.challenges_data["sysData"]["amountChallengePointForEasy"]:^{4}} ║")
    print(f"║{"  ==---> Нормальные испытания:    ":─<{Sizes.header}}║")
    for i in range(len(data.challenges_list["normal"])):
        print(f"║ {i+1:<{1}}. {challenge_status_feedback("normal", i)}  {crop_text(data.challenges_list["normal"][i], 80):<{82}}  {data.challenges_data["sysData"]["amountPointForNormal"]:<{3}} {data.challenges_data["sysData"]["amountChallengePointForNormal"]:^{4}} ║")
    print(f"║{"  ==---> Сложные испытания:    ":─<{Sizes.header}}║")
    for i in range(len(data.challenges_list["hard"])):
        print(f"║ {i+1:<{1}}. {challenge_status_feedback("hard", i)}  {crop_text(data.challenges_list["hard"][i], 80):<{82}}  {data.challenges_data["sysData"]["amountPointForHard"]:<{3}} {data.challenges_data["sysData"]["amountChallengePointForHard"]:^{4}} ║")
    print(f"║{"  ==---> БеЗуМнЫе иСпЫтАнИя:    ":─<{Sizes.header}}║")
    for i in range(len(data.challenges_list["insane"])):
        print(f"║ {i+1:<{1}}. {challenge_status_feedback("insane", i)}  {crop_text(data.challenges_list["insane"][i], 80):<{82}}  {data.challenges_data["sysData"]["amountPointForInsane"]:<{3}} {data.challenges_data["sysData"]["amountChallengePointForInsane"]:^{4}} ║")
    print(f"║{"  ==---> ДЕЕМОНЫ:    ":─<{Sizes.header}}║")
    for i in range(len(data.challenges_list["demonic"])):
        print(f"║ {i+1:<{1}}. {challenge_status_feedback("demonic", i)}  {crop_text(data.challenges_list["demonic"][i], 80):<{82}}  {data.challenges_data["sysData"]["amountPointForDemonic"]:<{3}} {data.challenges_data["sysData"]["amountChallengePointForDemonic"]:^{4}} ║")
    print(f"╟{"":─^{Sizes.header}}╢")
    print(f"║{"1 - Отметить задание выполненым. 0 - Главное меню.":^{Sizes.header}}║")
    print(end)
def chall_diff():
    clear()
    print(head)
    print(ac)
    print(division)
    print(f"╟{" Ежедневные Задания ":─^{Sizes.header}}╢")
    print(f"║{"":^{Sizes.header}}║")
    print(f"║{" Сейчас напиши сложность задания, которое выполнил.":^{Sizes.header}}║")
    print(f"║{" Следи за раскладкой своей клавиатуры, распознается только английский.":^{Sizes.header}}║")
    print(f"║{" Сложности: Easy, Normal, Hard, Insane, Demonic. Размер буквы не важен.":^{Sizes.header}}║")
    print(end)
def chall_num():
    clear()
    print(head)
    print(ac)
    print(division)
    print(f"╟{" Ежедневные Задания ":─^{Sizes.header}}╢")
    print(f"║{"":^{Sizes.header}}║")
    print(f"║{" Сейчас напиши только номер задания, которое выполнил.":^{Sizes.header}}║")
    print(f"║{" Следи за раскладкой своей клавиатуры, распознается только английский.":^{Sizes.header}}║")
    print(f"║{" Номера 1 или 2.":^{Sizes.header}}║")
    print(end)


def bonuses():
    clear()
    print(head)
    print(ac)
    print(division)
    print(f"╟{" Бонусы ":─^{Sizes.header}}╢")
    print(f"║{" -- Список ативных бонусов:":<{Sizes.header}}║")
    for i in range(2):
        print(f"║ {"Заглушка":<{Sizes.header-1}}║")
    print(f"║{" -- Доступные бонусы: ":<{Sizes.header}}║")
    for i in range(5):
        print(f"║ {"Заглушка":<{Sizes.header-1}}║")
    print(f"║{"":<{Sizes.header}}║")
    print(f"╟{"":─^{Sizes.header}}╢")
    print(f"║{"1 - Магазин бонусов. 2 - Рулетка бонусов. 3 - Описание. 0 - Меню.":<{Sizes.header}}║")
    print(end)
def shop():
    clear()
    print(head)
    print(ac)
    print(division)
    print(f"╟{" Магазин ":─^{Sizes.header}}╢")
    print(f"║{"":^{Sizes.header}}║")
    print(f"║║")

def more():
    clear()
    print(head)
    print(ac)
    print(division)
    print(f"╟{" Справка ":─^{Sizes.header}}╢")
    print(f"║{" - Общее:":<{Sizes.header}}║")
    print(f"║{" Задумка проста - выполняешь задания, набираешь 300 очков -- серия увеличивается.":<{Sizes.header}}║")
    print(f"║{" При наборе серии в 10 дней, получаешь доп. бонус.":<{Sizes.header}}║")
    print(f"║{" Есть раздел с заданиями, которые обновляются ежедневно и не отнимают много времени.":<{Sizes.header}}║")
    print(f"║{" Есть раздел с испытаниями, которые бросают тебе вызов, но и дают больше плюшек.":<{Sizes.header}}║")
    print(f"║{" Что бы отметить задание выполненым перейди в необходимый раздел и выбери задание(только честно)":<{Sizes.header}}║")
    print(f"║{" Это приложение всего лишь инструмент, если ты будешь 'читерить', то и оно не поможет тебе":<{Sizes.header}}║")
    print(f"║{" - Ежедневные задания:":<{Sizes.header}}║")
    print(f"║{" На выбор представлено 5 сложностей. За выполнение каждого задания начисляются очки.":<{Sizes.header}}║")
    print(f"║{" При 'Рерол'е заданий, прогресс сбрасывается вместе с набранными очками":<{Sizes.header}}║")
    print(f"║{" - Еженедельные испытания:":<{Sizes.header}}║")
    print(f"║{" Сложная версия некоторых ежедневных заданий. Список пополняется с обновлениями.":<{Sizes.header}}║")
    print(f"║{" Каждый тип сложности не только даёт разное количество очков, но и приближает тебя к бонусу. ":<{Sizes.header}}║")
    print(f"║{" Нельзя отметить выполненым более 2 в день и более 10 в неделю":<{Sizes.header}}║")
    print(end)
    input("Press enter to continue...")

def welcome_screen():
    clear()
    print(head)
    print(ac)
    print(f"╟{"         Добро пожаловать в обучение!        ":─^{Sizes.header}}╢")
    print(f"║{"  Привет Друг! Рад тебя видеть в этом приложении! Сейчас оно находится в стадии глубокой разработке.":<{Sizes.header}}║")
    print(f"║{" Будь готов к масштабным изменениям, или добавлениям большого количества функций.":<{Sizes.header}}║")
    print(f"║{" Ты уже знаешь о чем это приложение ты же читал описание? Надеюсь да.":<{Sizes.header}}║")
    print(f"║{" В общем я помогу тебе с самым стартом, пока это в текстовом формате, работу над интерфесом уже веду.":<{Sizes.header}}║")
    print(f"║{" Приложение пока не может и возможно даже в будущем не сможет отслеживать правдивость выполнения заданий, ноо":<{Sizes.header}}║")
    print(f"║{" я надеюсь на твою честность. ХЗ Почитай далее сам, постарался кратко.":<{Sizes.header}}║")
    print(f"║{"   ---  Общее:":<{Sizes.header}}║")
    print(f"║{" В приложении много чего, больше об этом узнаешь от компаньона, но самым важным являются режим:'Лагерь' и режим:'Приключение'":<{Sizes.header}}║")
    print(f"║{" Первый из названых более казуальный и простой, второй нацелен на историю и повествование.":<{Sizes.header}}║")
    print(f"║{" Выбирай то, что тебе по душе. Можешь почитать дальше о них подробнее если не интересно, просто пропусти.":<{Sizes.header}}║")
    print(f"║{"   ---  Интерфейс:":<{Sizes.header}}║")
    print(f"║{" Тут кратко по интерфейсу и расположению всего, что может бытсь отражено.":<{Sizes.header}}║")
    print(f"║{" Сверху, где идет заполнение единичной чертой - локация(меню) в котором ты находишься в данный момент.":<{Sizes.header}}║")
    print(f"║{" Сразу под этим в кавычках находится реплика твоего компаньона.":<{Sizes.header}}║")
    print(f"║{" После расположено основное информационное пространство.":<{Sizes.header}}║")
    print(f"║{" Ниже всего за такой же единичной полосой располагаются варианты действий":<{Sizes.header}}║")
    print(f"╟{"":─^{Sizes.header}}╢")
    print(f"╟{"Нажми Enter для перехода далее.":^{Sizes.header}}╢")
    print(end)
    input()
    clear()
    print(head)
    print(ac)
    print(f"╟{"   Обучение   ":─^{Sizes.header}}╢")
    print(f"║{"   ---  Лагерь:":<{Sizes.header}}║")
    print(f"║{" Это твоя постоянная обитель. Стартовый режим, который позволяет без напряжения узнавать механики.":<{Sizes.header}}║")
    print(f"║{" Тут ты сможешь просто поболтать со своим фамильяром, и следить за своим лагерем.":<{Sizes.header}}║")
    print(f"║{" Из лагеря ты можешь свободно перемещаться по локациям карты.":<{Sizes.header}}║")
    print(f"║{"   ---  Приключение:":<{Sizes.header}}║")
    print(f"║{" Режим для более смелых и целеустремленных людей, тут и задания тяжелее и их больше.":<{Sizes.header}}║")
    print(f"║{" Если ты один из таких, то докажи это. Приключения повествуют историю мира и персонажей.":<{Sizes.header}}║")
    print(f"╟{"":─^{Sizes.header}}╢")
    print(f"╟{"Нажми Enter для завершения обучения.":^{Sizes.header}}╢")
    print(end)
    input()
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def task_status_feedback(diff, num):
    tasks_stat = data.task_statuses
    if tasks_stat[diff][f"is{num}TaskComplete"]:
        return "Выполнено."
    else:
        return "Не выполнено."
def challenge_status_feedback(diff, num):
    chall_stat = data.challenges_statuses
    if chall_stat[diff][f"is{num}Complete"]:
        return "✔"
    else:
        return "✖"
def crop_text(text, max_length):
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."
def campfire():
    clear()
    print(head)
    print(ac)
    print(division)
    print(f"╟{" Лагерь ":─^{Sizes.header}}╢")
    print(f"║{' """ Реплика фамильяра """    ':>{Sizes.header}}║")
    print(f"║{"    Костер горящий в центре лагеря(log:)":<{Sizes.header}}║")
    print(f"║{"    Твой ФАМИЛЬЯР занятый(log:)":<{Sizes.header}}║") #возможно переписать под разные занятия инного
    print(f"║{"    Стоит доска объявлений и на ней видны висящие листки":<{Sizes.header}}║")
    print(f"║{"    Рюкзаки с котелками и другими вещами":<{Sizes.header}}║")
    print(f"║{"    Потрепанная карта, лежащая у входа в палатку":<{Sizes.header}}║")
    print(f"╟{"":─^{Sizes.header}}╢")
    print(f"║{" Костер - 1 | ФАМИЛЬЯР - 2 | Доска объявлений - 3 | Снаряжение - 4 | Карта - 5 ":^{Sizes.header}}║")
    print(end)