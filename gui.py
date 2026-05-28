import os
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
    input("<UNK>")

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
    input("")
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