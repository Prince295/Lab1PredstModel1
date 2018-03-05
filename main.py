from functions import *
from models import *
first_choice = {1 : "Добавить",
                    2 : "Моделирование"}
second_choice = {1 : "Организаторы",
                 2 : "Гости"}
set_dishes()
set_drinks()
set_entertaiment()

def main_menu():
    choice = input_numbers(first_choice, "Меню")
    if choice == 1:
        choice2 = input_numbers(second_choice, "Добавление")
        if choice2 == 1:
            set_organisator()
        else:
            set_guest()
    else:
        print("Выбор организаторов")
        choice_organisator_dict, choice_organisator_number =  input_mutch(get_names(org))
        print("Выбор гостей")
        choice_guest_dict, choice_guest_number = input_mutch(get_names(guest_dict))
        set_event()
        org_ratio=get_organisator_ratio()
        point = 0
        for key, val in choice_organisator_dict:
            point+=org_ratio[val]
        point/=choice_organisator_number
        if point<8:


        else:
        modulate_event()




