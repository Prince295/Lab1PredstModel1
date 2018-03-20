import numpy as np

from functions import *
from models import *

first_choice = {1 : "Редактировать",
                2 : "Моделирование",
                3 : "Выход"}
second_choice = {1 : "Организаторы",
                 2 : "Гости",
                 3 : "Вернуться в главное меню"}
third_choice = {1 : "Добавить",
                2 : "Удалить",
                3 : "Вернуться в главное меню"}
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
            choice2 = input_numbers(second_choice, "Редактирование")
            if choice2 == 1:
                choice3 = input_numbers(third_choice, "Добавить/удалить")
                if choice3 == 1:
                    set_organisator()
                elif choice3 == 2:
                    for k in org.keys():
                        print(k)
                    if is_ok() == False:
                        continue
                    delete_person(org,"Удаление организатора", 'organisators.txt')
                else:
                    continue
            elif choice2== 2:
                choice3 = input_numbers( third_choice, "Добавить/удалить" )
                if choice3 == 1:
                    set_guest()
                elif choice3 == 2:
                    for k in guest_dict.keys():
                        print(k)
                    if is_ok() == False:
                        continue
                    delete_person( guest_dict, "Удаление гостя", 'guests.txt' )
                else:
                    continue
            else:
                continue

        #Ветвь моделирования
        elif choice== 2:
            print("Выбор организаторов")
            for k,v in get_names(org).items():
                print("Организатор {} : \n Образование  - {} \n Портфолио  - {} \n Характер  - {} \n Возраст  - {} \n".format(v,
                                                                                                               Person.education[int(org[v]['Education'])],
                                                                                                               Person.portfolio[int(org[v]['Portfolio'])],
                                                                                                               Person.temper[int(org[v]['Temper'])],
                                                                                                               org[v]['Age']) )
            if is_ok() == False:
                continue
            choice_organisator_dict, choice_organisator_number =  input_mutch(get_names(org)) #считываем выбранных организаторов
            print("Выбор гостей")
            if is_ok() == False:
                continue
            choice_guest_dict, choice_guest_number = input_mutch(get_names(guest_dict)) #считываем выбранных гостей
            event_duration = set_event() # запуск функции генерации праздников
            org_ratio=get_organisator_ratio() #получаем коэффициенты характеристик организаторов
            point = 0
            budget = 0
            overall_enjoy=1
            mark = 0

            # считаем бюджет и "уровень" организатора
            for key, val in choice_organisator_dict.items():
                point+=int(org_ratio[val])

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
            budget = budget + place[mark].price
            point/=choice_organisator_number
            # Ветвь успешных организаторов
            if point<8:

                # В словаре выбранных гостей оцениваем их предпочтения, исходя из социального статуса
                # , подсчитываем бюджет и составляем меню
                timer = event_duration
                while event_duration > 0:


                    for key, val in choice_guest_dict.items():
                        if timer > 0:
                            i = np.random.randint( len( entertaiment ) )
                            if entertaiment[i].duration < event_duration:
                                timer = entertaiment[i].duration
                                guest_dict[val]['Sentiment'] = int(
                                    get_enjoing_entertaiment( guest_dict[val], entertaiment[i] ) ) + int(
                                    guest_dict[val]['Sentiment'] )
                                count.entertaiments[entertaiment[i].name] += 1
                        # Студенты
                        if guest_dict[val]['Social_status'] == '1':
                            flag1=0
                            flag2=0
                            while True:
                                i = np.random.randint(len(drink))
                                if drink[i].alcohol == "Да":
                                    flag1 = i
                                    flag2 = drink[i].price
                                    break
                            guest_dict[val]['Sentiment'] = int(get_enjoing_drink(guest_dict[val], drink[flag1])) + int(guest_dict[val]['Sentiment'])
                            budget = budget + drink[flag1].price
                            count.drinks[drink[flag1].name]+=1
                            flag1=0
                            flag2=0
                            while True:
                                i = np.random.randint( len( dish ) )
                                if dish[i].consistency['Жиры'] > 55:
                                    flag1=i
                                    break
                            guest_dict[val]['Sentiment'] = int(get_enjoing_dish( guest_dict[val],
                                                                                     dish[flag1] ))+int(guest_dict[val]['Sentiment'])
                            budget = budget + dish[flag1].price
                            count.dishes[dish[flag1].name]+=1


                        # Школьники
                        if guest_dict[val]['Social_status'] == '2':
                            flag1 = 0
                            flag2 = 0
                            for i in range( len( drink ) ):
                                if drink[i].alcohol == "Нет":
                                    if drink[i].price > flag2:
                                        flag1 = i
                                        flag2 = drink[i].price
                            guest_dict[val]['Sentiment'] = int(get_enjoing_drink(guest_dict[val], drink[flag1])) + int(guest_dict[val]['Sentiment'])
                            budget = budget + drink[flag1].price
                            count.drinks[drink[flag1].name]+=1
                            flag1 = np.random.randint(len(dish))
                            guest_dict[val]['Sentiment'] = int(get_enjoing_dish( guest_dict[val],
                                                                                     dish[flag1] ))+int(guest_dict[val]['Sentiment'])
                            budget = budget + dish[flag1].price
                            count.dishes[dish[flag1].name]+=1

                        # Начинающие работники
                        if guest_dict[val]['Social_status'] == '3':
                            flag1 = 0
                            flag2 = 0
                            while True:
                                i = np.random.randint(len(drink))
                                if drink[i].alcohol == "Да":
                                    flag1 = i
                                    flag2 = drink[i].price
                                    break
                            guest_dict[val]['Sentiment'] = int(get_enjoing_drink(guest_dict[val], drink[flag1])) + int(guest_dict[val]['Sentiment'])
                            budget = budget + drink[flag1].price
                            count.drinks[drink[flag1].name]+=1
                            flag1 = 0
                            flag2 = 0
                            for i in range( len( dish ) ):
                                if dish[i].consistency['Белки'] > flag2:
                                    flag1 = i
                                    flag2 = dish[i].consistency['Белки']
                            guest_dict[val]['Sentiment'] = int(get_enjoing_dish( guest_dict[val],
                                                                                     dish[flag1] ))+int(guest_dict[val]['Sentiment'])
                            budget = budget + dish[flag1].price
                            count.dishes[dish[flag1].name]+=1


                        # Работники со стажем
                        if guest_dict[val]['Social_status'] == '4':
                            flag1 = 0
                            flag2 = 0
                            while True:
                                i = np.random.randint(len(drink))
                                if drink[i].alcohol == "Да":
                                    flag1 = i
                                    flag2 = drink[i].price
                                    break
                            guest_dict[val]['Sentiment'] = int(get_enjoing_drink(guest_dict[val], drink[flag1])) + int(guest_dict[val]['Sentiment'])
                            budget = budget + drink[flag1].price
                            count.drinks[drink[flag1].name] += 1
                            flag1 = 0
                            while True:
                                i = np.random.randint( len( dish ) )
                                if dish[i].consistency['Каллорийность'] < 360:
                                    flag1=i
                                    break
                            guest_dict[val]['Sentiment'] = int(get_enjoing_dish( guest_dict[val],
                                                                                     dish[flag1] ))+int(guest_dict[val]['Sentiment'])
                            budget = budget + dish[flag1].price
                            count.dishes[dish[flag1].name]+=1

                        # Пенсионеры
                        if guest_dict[val]['Social_status'] == '5':
                            flag1 = 0
                            flag2 = 99999
                            for i in range( len( drink ) ):
                                if drink[i].alcohol == "Нет":
                                    if drink[i].price < flag2:
                                        flag1 = i
                                        flag2 = drink[i].price

                            guest_dict[val]['Sentiment'] = int(get_enjoing_drink(guest_dict[val], drink[flag1])) + int(guest_dict[val]['Sentiment'])
                            budget = budget + drink[flag1].price
                            count.drinks[drink[flag1].name]+=1
                            flag1 = 0
                            flag2 = 99999
                            for i in range( len( dish ) ):
                                if dish[i].consistency['Жиры'] < flag2:
                                    flag1 = i
                                    flag2 = dish[i].consistency['Жиры']

                            guest_dict[val]['Sentiment'] = int(get_enjoing_dish( guest_dict[val],
                                                                                     dish[flag1] ))+int(guest_dict[val]['Sentiment'])
                            budget = budget + dish[flag1].price
                            count.dishes[dish[flag1].name]+=1

                    event_duration = event_duration - 30
                    timer = timer - 30


            #Ветвь выбора праздника от неуспешных организаторов
            else:
                timer = event_duration
                while event_duration>0:

                    for key, val in choice_guest_dict.items():
                        if timer > 0:
                            i = np.random.randint( len( entertaiment ) )
                            if entertaiment[i].duration < event_duration:
                                timer = entertaiment[i].duration
                                guest_dict[val]['Sentiment'] = int( get_enjoing_entertaiment( guest_dict[val],
                                                                                              entertaiment[i] ) ) + int(
                                    guest_dict[val]['Sentiment'] )
                                count.entertaiments[entertaiment[flag1].name] += 1

                        flag1 = np.random.randint(len(drink))
                        budget = budget + drink[flag1].price
                        count.drinks[drink[flag1].name]+=1
                        flag1 = np.random.randint(len(dish))
                        budget = budget + dish[flag1].price
                        count.dishes[dish[flag1].name]+=1
                    event_duration = event_duration - 30
                    timer = timer - 30
            # вывод на результатов моделирования на экран
            print("Адрес места проведения")
            print(place[mark].address)
            print("Потраченный бюджет")
            print(budget)
            print( "Количество гостей" )
            print( choice_guest_number )
            print("Меню")
            print(count.dishes)
            print(count.drinks)
            print("Список развлечений")
            print(count.entertaiments)
            for name, attributes in choice_guest_dict.items():
                val = guest_dict[attributes]["Sentiment"]
                charact = 'Вне себя от злости'
                for k,v in sentiment_ratio.items():
                    if int(val)>v:
                        charact = k
                        break
                    if int(val)<=0:
                        break
                print(" {} : {}".format(attributes, charact))
                guest_dict[attributes]["Sentiment"] = sentiment_ratio[charact]
            f = open( 'guests.txt', 'w' )
            for key, val in guest_dict.items():
                f.write( '{}:{}\n'.format( key, val ) )
            f.close()
        else:
            break

if __name__ == '__main__':
    main_menu()




