import json
import gui, data

def shop():
    choises= {
    "1": bonus_add
    }
    gui.shop()
    userchoice = input("Press 1 to continue...")
    if userchoice in choises:
        action = choises.get(userchoice)
        action()

def burmalda():
    print("Burmalda")
    input("Press enter to continue...")

def description():
    print("Description")
    input("Press enter to continue...")

#костыль
#Перенести в debug.py
def bonus_add():
    print("Bonus Add")
    id = input("ID: ")
    name = input("Name: ")
    rarity = input("Rarity: ")
    description = input("Description: ")
    effect = input("Effect: ")
    duration = int(input("Duration: "))
    price = int(input("Price: "))
    shopperDescription = input("Shopper Description: ")
    newBonus = {
        f"{id}": {
            "name": name,
            "rarity": rarity,
            "description": description,
            "effect": effect,
            "duration": duration,
            "price": price,
            "shopperDescription": shopperDescription
        }
    }
    data.bonusdata.update(newBonus)
    with open('cache/bonuses/bonus_data.json', 'w', encoding='utf-8') as f:
        json.dump(data.bonusdata, f, ensure_ascii=False, indent=2)