from functions import *
from models import *
import numpy as np
first_choice = {1 : "Добавить",
                2 : "Моделирование"}
second_choice = {1 : "Организаторы",
                 2 : "Гости"}
set_dishes()
set_drinks()
set_entertaiment()
set_place()
set_count()


def main_menu():
    # Ветвь добавления Организаторов и гостей
    while True:
        choice = input_numbers(first_choice, "Меню")
        if choice == 1:
            choice2 = input_numbers(second_choice, "Добавление")
            if choice2 == 1:
                set_organisator()
            else:
                set_guest()

        #Ветвь моделирования
        else:
            print("Выбор организаторов")
            choice_organisator_dict, choice_organisator_number =  input_mutch(get_names(org))
            print("Выбор гостей")
            choice_guest_dict, choice_guest_number = input_mutch(get_names(guest_dict))
            set_event()
            print(org)
            org_ratio=get_organisator_ratio()
            point = 0
            budget = 0
            overall_enjoy=1
            mark = 0

            # считаем бюджет и "уровень" организатора
            for key, val in choice_organisator_dict.items():
                point+=int(org_ratio[val])
                budget+=int(org[val]['Budget'])

            #Выбираем место проведения
            for i in range(len(place)):
                if choice_guest_number <= place[i].capacity:
                    for key, val in choice_guest_dict.items():
                        if guest_dict[val]['Social_status'] == '1':
                            count.guests['Студент']+=1
                        if guest_dict[val]['Social_status'] == '2':
                            count.guests['Школьник']+=1
                        if guest_dict[val]['Social_status'] == '3':
                            count.guests['Начинающий работник']+=1
                        if guest_dict[val]['Social_status'] == '4':
                            count.guests['Работник со стажем']+=1
                        if guest_dict[val]['Social_status'] == '5':
                            count.guests['Пенсионер']=+1
                    max_guests=0
                    index =''
                    for key, val in count.guests.items():
                        if count.guests[key]>max_guests:
                            max_guests = count.guests[key]
                            index = key
                    if index == 'Школьник' and place[i].design == 'Детский':
                        mark = i
                        break
                    else:
                        mark = np.random.randint(len(place)-1)

            #Вычет из бюджета цены аренды помещения и подсчет уровня каждого организатора по отдельности
            budget = budget - place[mark].price
            point/=choice_organisator_number
            # Ветвь успешных организаторов
            if point<8:
                budget = budget/choice_guest_number
                # В словаре выбранных гостей оцениваем их предпочтения, исходя из социального статуса
                # , подсчитываем бюджет и составляем меню
                for key, val in choice_guest_dict.items():
                    # Студенты
                    if guest_dict[val]['Social_status'] == '1':
                        flag1=0
                        flag2=0
                        for i in range(len(drink)):
                            if drink[i].alcohol == "Да":
                                if drink[i].price > flag2:
                                    flag1 = i
                                    flag2 = drink[i].price
                        budget = budget - drink[flag1].price
                        if int(budget) > 0:
                            count.drinks[drink[flag1].name]+=1
                        flag1=0
                        flag2=0
                        for i in range(len(dish)):
                            if dish[i].consistency['Жиры'] > flag2:
                                flag1=i
                                flag2=dish[i].consistency['Жиры']
                        budget = budget - dish[flag1].price
                        if int(budget) > 0:
                            count.dishes[dish[flag1].name]+=1
                        flag1=0
                        flag2=0
                        for i in range(len(entertaiment)):
                            if entertaiment[i].activity == "Высокая физическая активность":
                                if entertaiment[i].duration > flag2:
                                    flag1 = i
                                    flag2 = entertaiment[i].duration
                        count.entertaiments[entertaiment[flag1].name]+=1

                    # Школьники
                    if guest_dict[val]['Social_status'] == '2':
                        flag1 = 0
                        flag2 = 0
                        for i in range( len( drink ) ):
                            if drink[i].alcohol == "Нет":
                                if drink[i].price > flag2:
                                    flag1 = i
                                    flag2 = drink[i].price
                        budget = budget - drink[flag1].price
                        if int(budget) > 0:
                            count.drinks[drink[flag1].name]+=1
                        flag1 = np.random.randint(len(drink))
                        budget = budget - drink[flag1].price
                        if int(budget) > 0:
                            count.dishes[dish[flag1].name]+=1
                        flag1 = 0
                        flag2 = 0
                        for i in range( len( entertaiment ) ):
                            if entertaiment[i].activity == "Высокая физическая активность":
                                if entertaiment[i].duration > flag2:
                                    flag1 = i
                                    flag2 = entertaiment[i].duration
                        count.entertaiments[entertaiment[flag1].name]+=1

                    # Начинающие работники
                    if guest_dict[val]['Social_status'] == '3':
                        flag1 = 0
                        flag2 = 0
                        for i in range( len( drink ) ):
                            if drink[i].alcohol == "Есть":
                                if drink[i].price > flag2:
                                    flag1 = i
                                    flag2 = drink[i].price
                        budget = budget - drink[flag1].price
                        count.drinks[drink[flag1].name]+=1
                        flag1 = 0
                        flag2 = 0
                        for i in range( len( dish ) ):
                            if dish[i].consistency['Белки'] > flag2:
                                flag1 = i
                                flag2 = dish[i].consistency['Белки']
                        budget = budget - dish[flag1].price
                        count.dishes[dish[flag1].name]+=1
                        flag1 = 0
                        flag2 = 999999
                        for i in range( len( entertaiment ) ):
                            if entertaiment[i].activity == "Средняя физическая активность":
                                if entertaiment[i].duration < flag2:
                                    flag1 = i
                                    flag2 = entertaiment[i].duration
                        count.entertaiments[entertaiment[flag1].name]+=1

                    # Работники со стажем
                    if guest_dict[val]['Social_status'] == '4':
                        flag1 = 0
                        flag2 = 0
                        for i in range( len( drink ) ):
                            if drink[i].alcohol == "Есть":
                                if drink[i].price > flag2:
                                    flag1 = i
                                    flag2 = drink[i].price
                        budget = budget - drink[flag1].price
                        count.drinks[drink[flag1].name]+=1
                        flag1 = 0
                        flag2 = 99999
                        for i in range( len( dish ) ):
                            if dish[i].consistency['Каллорийность'] < flag2:
                                flag1 = i
                                flag2 = dish[i].consistency['Каллорийность']
                        budget = budget - dish[flag1].price
                        count.dishes[dish[flag1].name]+=1
                        flag1 = 0
                        flag2 = 0
                        for i in range( len( entertaiment ) ):
                            if entertaiment[i].activity == "Низкая физическая активность":
                                if entertaiment[i].duration > flag2:
                                    flag1 = i
                                    flag2 = entertaiment[i].duration
                        count.entertaiments[entertaiment[flag1].name]+=1

                    # Пенсионеры
                    if guest_dict[val]['Social_status'] == '5':
                        flag1 = 0
                        flag2 = 99999
                        for i in range( len( drink ) ):
                            if drink[i].alcohol == "Нет":
                                if drink[i].price < flag2:
                                    flag1 = i
                                    flag2 = drink[i].price
                        budget = budget - drink[flag1].price
                        count.drinks[drink[flag1].name]+=1
                        flag1 = 0
                        flag2 = 99999
                        for i in range( len( dish ) ):
                            if dish[i].consistency['Жиры'] < flag2:
                                flag1 = i
                                flag2 = dish[i].consistency['Жиры']
                        budget = budget - dish[flag1].price
                        count.dishes[dish[flag1].name]+=1
                        flag1 = 0
                        flag2 = 99999
                        for i in range( len( entertaiment ) ):
                            if entertaiment[i].activity == "Низкая физическая активность":
                                if entertaiment[i].duration < flag2:
                                    flag1 = i
                                    flag2 = entertaiment[i].duration
                        count.entertaiments[entertaiment[flag1].name]+=1

            #Ветвь выбора праздника от неуспешных организаторов
            else:
                budget = budget / choice_guest_number
                for key, val in choice_guest_dict:
                    flag1 = np.random.randint(len(drink))
                    budget = budget - drink[flag1].price
                    if int(budget) > 0:
                        count.drinks[drink[flag1].name]+=1
                    flag1 = np.random.randint(len(dish))
                    budget = budget - dish[flag1].price
                    if int(budget) > 0:
                        count.dishes[dish[flag1].name]+=1
                    flag1 = np.random.randint(len(entertaiment))
                    budget = budget - entertaiment[flag1].price
                    if int(budget) > 0:
                        count.entertaiments.update({entertaiment[flag1].name:count.entertaiments[entertaiment[flag1].name]+1})

            print(place[mark].address)
            print(budget)
            print(count.dishes)
            print(count.drinks)
            print(count.guests)
            print(count.entertaiments)
            print(point)

if __name__ == '__main__':
    main_menu()




