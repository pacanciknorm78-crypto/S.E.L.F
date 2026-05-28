import os, data
"""   operators && classes   """
#print(f"║{"":^{Sizes.header}}║")
head     = "╔════════════════════════════════════════════════════════════════════════════════════════════════════╗"
division = "╠════════════════════════════════════════════════════════════════════════════════════════════════════╣"
end      = "╚════════════════════════════════════════════════════════════════════════════════════════════════════╝"
class Sizes:
    header = 100

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
        print(f"║ {num:<{3}} {text:<{62}} {points:>{6}}          {status:<{15}} ║")
    print(f"║{"  ==-->  Сложность класса В:   ":─<{Sizes.header - 3}}   ║")
    for i in range(len(data.tasklist["b"])):
        text = data.tasklist["b"][i]
        num = f'{i+1}.'
        points = 20
        status = task_status_feedback("b", i+1)
        print(f"║ {num:<{3}} {text:<{62}} {points:>{6}}          {status:<{15}} ║")
    print(f"║{"  ==-->  Сложность класса A:   ":─<{Sizes.header - 3}}   ║")
    for i in range(len(data.tasklist["a"])):
        text = data.tasklist["a"][i]
        num = f'{i + 1}.'
        points = 50
        status = task_status_feedback("a", i+1)
        print(f"║ {num:<{3}} {text:<{62}} {points:>{6}}          {status:<{15}} ║")
    print(f"║{"  ==-->  Сложность класса S:   ":─<{Sizes.header - 3}}   ║")
    for i in range(len(data.tasklist["s"])):
        text = data.tasklist["s"][i]
        num = f'{i + 1}.'
        points = 100
        status = task_status_feedback("s", i+1)
        print(f"║ {num:<{3}} {text:<{62}} {points:>{6}}          {status:<{15}} ║")
    print(f"║{"  ==-->  Сложность класса SS:   ":─<{Sizes.header - 3}}   ║")
    for i in range(len(data.tasklist["ss"])):
        text = data.tasklist["ss"][i]
        num = f'{i + 1}.'
        points = 150
        status = task_status_feedback("ss", i+1)
        print(f"║ {num:<{3}} {text:<{62}} {points:>{6}}          {status:<{15}} ║")
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
    print(f"║{"SelfControlling App by Takimka":^{Sizes.header}}║")
    print(division)
    print(f"╟{" Ежедневные Задания ":─^{Sizes.header}}╢")
    print(f"║{"":^{Sizes.header}}║")
    print(f"║{" Все задания сброшены, прогресс утерян":^{Sizes.header}}║")
    print(end)


def challenges():
    clear()
    print(head)
    print(f"║{"SelfControlling App by Takimka":^{Sizes.header}}║")
    print(division)
    input("<UNK>")

def bonuses():
    clear()
    print(head)
    print(f"║{"SelfControlling App by Takimka":^{Sizes.header}}║")
    print(division)
    input("<UNK>")



def more():
    clear()
    print(head)
    print(f"║{"SelfControlling App by Takimka":^{Sizes.header}}║")
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
def menu():
    clear()
    print(head)
    print(f"║{"SelfControlling App by Takimka":^{Sizes.header}}║")
    print(division)
    print(f"║{"Приложение позволяет улучшить свой самоконтроль, путем поставления простеньких заданий.":^{Sizes.header}}║")
    print(f"╟{" Навигация ":─^{Sizes.header}}╢")
    print(f"║{"    Перейти к ежедневным заданиям  --  1":<{Sizes.header}}║")
    print(f"║{"    Перейти к еженедельным испытаниям  --  2":<{Sizes.header}}║")
    print(f"║{"    Перейти к бонусам  --  3":<{Sizes.header}}║")
    print(f"║{"    Вернуться назад в меню  --  0":<{Sizes.header}}║")
    print(f"║{"    Справка  --  9":<{Sizes.header}}║")
    print(end)
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def task_status_feedback(diff, num):
    tasks_stat = data.task_statuses
    if tasks_stat[diff][f"is{num}TaskComplete"]:
        return "Выполнено."
    else:
        return "Не выполнено."