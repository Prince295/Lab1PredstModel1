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
        budget = 0
        count = Count
        overall_enjoy=1
        for key, val in choice_organisator_dict:
            point+=org_ratio[val]
            budget+=org[val]['Budget']
        point/=choice_organisator_number
        if point<8:
            budget/choice_guest_number
            for key, val in choice_guest_dict:
                if guest_dict[val]['Social_status'] == 1:
                    flag1=0
                    flag2=0
                    for i in range(len(drink)):
                        if drink[i].alcohol == "Есть":
                            if drink[i].price > flag2:
                                flag1 = i
                                flag2 = drink[i].price
                    budget = budget - drink[flag1].price
                    count.drinks[drink[flag1].name]+=1
                    flag1=0
                    flag2=0
                    for i in range(len(dish)):
                        if dish[i].consistency['Жиры'] > flag2:
                            flag1=i
                            flag2=dish[i].consistency['Жиры']
                    budget = budget - dish[flag1].price
                    count.dishes[dish[flag1].name]+=1

                if guest_dict[val]['Social_status'] == 2:
                if guest_dict[val]['Social_status'] == 3:
                if guest_dict[val]['Social_status'] == 4:
                if guest_dict[val]['Social_status'] == 5:




        else:





