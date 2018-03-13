from functions import *
from models import *
import numpy as np
first_choice = {1 : "Добавить",
                2 : "Моделирование",
                3 : "Выход"}
second_choice = {1 : "Организаторы",
                 2 : "Гости"}
set_dishes()
set_drinks()
set_entertaiment()
set_place()
set_count()


def main_menu():
    while True:
        f1 = open( "organisators.txt", 'r' ) #Открываем файл
        f3 = open( "guests.txt", 'r' )
        for i in f1.readlines(): #Читаем построчно
            key, val = i.strip().split( ':', maxsplit=1 ) #Разделяем ОДИН раз по разделителю - двоеточие
            val = val[1:len( val ) - 1] #Удаляем { и }
            val = re.sub( r"\'", '', val ) # замена кавычек
            val = re.sub( r',', ":", val ) # замена запятых
            list1 = []
            list1 = val.strip().split( ':' ) #разделяем по двоеточиям без ограничений
            for i in range( len( list1 ) ): #удаляем пробелы в начале элементов
                if list1[i][0] == ' ':
                    list1[i] = list1[i][1:]
            l = 0
            val = {}
            while l <= len( list1 ) - 2: #нечетные элементы списка - ключи словаря, четные - значения
                val[list1[l]] = list1[l + 1]
                l += 2
            org[key] = val #составляем словарь
        for i in f3.readlines():
            key, val = i.strip().split( ':', maxsplit=1 )
            val = val[1:len( val ) - 1]
            val = re.sub( r"\'", '', val )
            val = re.sub( r',', ":", val )
            list1 = []
            list1 = val.strip().split( ':' )
            for i in range( len( list1 ) ):
                if list1[i][0] == ' ':
                    list1[i] = list1[i][1:]
            l = 0
            val = {}
            while l <= len( list1 ) - 2:
                val[list1[l]] = list1[l + 1]
                l += 2
            guest_dict[key] = val
        f1.close()
        f3.close()
        choice = input_numbers(first_choice, "Меню")
        # Ветвь добавления Организаторов и гостей
        if choice == 1:
            choice2 = input_numbers(second_choice, "Добавление")
            if choice2 == 1:
                set_organisator()
            else:
                set_guest()


        #Ветвь моделирования
        elif choice== 2:
            print("Выбор организаторов")
            choice_organisator_dict, choice_organisator_number =  input_mutch(get_names(org)) #считываем выбранных организаторов
            print("Выбор гостей")
            choice_guest_dict, choice_guest_number = input_mutch(get_names(guest_dict)) #считываем выбранных гостей
            set_event() # запуск функции генерации праздников
            org_ratio=get_organisator_ratio() #получаем коэффициенты характеристик организаторов
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
                    for key, val in choice_guest_dict.items(): #считаем гостей по социальному статусу
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
                        if count.guests[key]>max_guests: #находим наиболее часто встречающуюся социальную группу
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
            # вывод на результатов моделирования на экран
            print("Адрес места проведения")
            print(place[mark].address)
            print("Остаток бюджета")
            print(budget)
            print( "Количество гостей" )
            print( choice_guest_number )
            print("Меню")
            print(count.dishes)
            print(count.drinks)
            print("Список развлечений")
            print(count.entertaiments)
        else:
            break

if __name__ == '__main__':
    main_menu()




