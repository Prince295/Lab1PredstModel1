import pickle
import re

from models import *

org = {}
guest_dict = {}
event_dict = {}
drink = []
dish = []
entertaiment=[]
place = []
count = Count
f1 = open( "organisators.txt", 'r' )
f3 = open( "guests.txt", 'r' )
for i in f1.readlines():
    key,val = i.strip().split( ':', maxsplit=1)
    val = val[1:len(val)-1]
    val = re.sub(r"\'", '', val )
    val = re.sub(r',', ":", val)
    list1=[]
    list1 = val.strip().split(':')
    for i in range(len(list1)):
        if list1[i][0]==' ':
            list1[i] = list1[i][1:]
    l = 0
    val = {}
    while l <= len(list1)-2:
        val[list1[l]] = list1[l+1]
        l+=2
    org[key] = val
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

# Выбор вариантов ответа
def input_numbers(dictionary, label):
    while True:
        print( label )
        for item in dictionary.keys():
            print( "{} - {}".format( item, dictionary[item] ) )
        x = input( "Введите вариант" )
        try:
            x = int( x ) #Проверка корректности ввода числа
        except ValueError:
            print( "Это не число. Пожалуйста, введите число, соответствующее номеру варианта " )
            continue

        for item in dictionary.keys(): #перебор ключей в словаре. Проверяем есть ли такой вариант ответа
            if x==item:
                return int( x )
                break
        else:
            print( "Введите число, соответсвующее номеру варианта" )

# Ввод целого числа
def input_number(param):
    print( param )
    while True:
        x = input( "Введите целое число" )
        try:
            x = int( x ) #Проверка корректности ввода числа
        except ValueError:
            print( "Это не целое число. Пожалуйста, введите число" )
            continue
        return x

#     проверяем корректность введенного числа в контексте вариантов ответа
def correct_number(param,dictionary):
    while True:
        number = input_number(param)
        if number > len(dictionary): #Сравнение введенного числа с количеством вариантов выбора
            print("Значение больше количества вариантов выбора")
            print("Количество вариантов = {}".format(len(dictionary)))
        elif number <=0:
            print("Вы не выбрали ничего. Пожалуйста введите корректное положительное число")
        else:
            break
    return number


def input_date(label):
    while True:
        print( label )
        date = input( "Введите дату в формате dd-mm-gggg " )
        result = re.findall( r'\d{2}[-./:]\d{2}[-./:]\d{4}', date ) #проверка введенной строки на соответствие шаблону даты
        if result == []:
            print( "Введите дату в корректном формате" )
        else:
            day, month, year = re.split( r'[-./:]', result[0], maxsplit=2 ) #Разделяем строку с датой на день, месяц, год
            if (0 < int( day ) < 32) and (0 < int( month ) < 13) and (2017 < int( year ) < 2099):
                return "{}.{}.{}".format( day, month, year ) #Возвращаем дату в виде строки
                break
            else:
                print( "Такой даты не существует, или запись на данную дату невозможна" )


def input_mutch(dictionary): #Функция выбора вариантов в словаре. После выбора словарь обновляется. Выбранный вариант удаляется. Результаты выбора возвращаются
    out_dict = {}
    number = correct_number( "Количество людей",dictionary ) #Получаем количество выбранных персон
    for i in range( number ):
        add = input_numbers( dictionary, 'Выбор' ) #Вывод меню с вариантами и выбор варианта пользователем
        for key, val in dictionary.items(): #обращаемся к словарю с вариантами
            out_dict.update({add : dictionary[add]}) #заносим результаты выбора в новый словарь
        dictionary.pop( add ) #Удаляем из словаря с вариантами выбора выбранный вариант
    return out_dict, number #Возвращаем словарь с выбранными персонами и количество выбранных персон

def set_organisator(): #Функция добавления пользователем нового организатора
    case1 = Organisator( input_numbers( Organisator.amount,Organisator.amount_label.__str__() ), 0 )
    if case1.amount == 2: #Проверка того, один ли это человек или группа людей
        case1.numbers = input_number( case1.numbers_label.__str__() )
    else:
        case1.numbers=1
    for i in range( case1.numbers ): #Цикл с количеством повторений, равным количеству добавляемых людей
        key = input( "Введите имя" )
        value = {'Education': input_numbers( Person.education, Person.education_label.__str__() ),
                 'Portfolio': input_numbers( Person.portfolio, Person.portfolio_label.__str__() ),
                 'Age': input_number( Person.age_label.__str__() ),
                 'Appearance': input_numbers( Person.appearance, Person.appearance_label.__str__() ),
                 'Sex': input_numbers( Person.sex, Person.sex_label.__str__() ),
                 'Speciality': input_numbers( Person.speciality, Person.speciality_label.__str__() ),
                 'Temper': input_numbers( Person.temper, Person.temper_label.__str__() ),
                 } #Создание словаря в словаре "Организатор"

        org.update( {key: value} )
        # value.clear()
    f = open( 'organisators.txt', 'a' ) #Открываем файл на добавление
    for key, val in org.items():
        f.write( '{}:{}\n'.format( key, val ) )
    f.close()

def delete_person(dictionary, label,textfile):
    dictionary.pop(get_names(dictionary)[input_numbers(get_names(dictionary),label)])
    f = open( textfile, 'w' )
    for key, val in dictionary.items():
        f.write( '{}:{}\n'.format( key, val ) )
    f.close()
    return dictionary
def is_ok():
    ok={1 : 'Продолжить',
        2 : 'Вернуться'}
    if input_numbers(ok,"Хотите продолжить?") == 1:
        return True
    else:
        return False



def get_names(dictionary): #Функция преобразования словаря вида {Имя : параметры} в словарь вида {число : имя} для меню выбора
    names = {}
    i = 1
    for item in dictionary.keys():
        names[i] = item
        i += 1
    return names




def set_guest(): #Добавление гостя. Все аналогично добавлению организатора
    case2 = Guest
    case2.amount = input_number( case2.amount_label.__str__() )
    for i in range( case2.amount ):
        key = input( "Введите имя" )
        value = {'Temper': input_numbers( Human.temper, Human.temper_label.__str__() ),
                 'Social_status': input_numbers( Human.social_status, Human.social_status_label.__str__() ),
                 'Age': input_number( Human.age_label.__str__() ),
                 'Sex': input_numbers( Human.sex, Human.sex_label.__str__() ),
                 'Sentiment' : sentiment_ratio[sentiment[input_numbers(sentiment,"Настроение гостя")]]}
        guest_dict.update( {key: value} )
    f = open( 'guests.txt', 'a' )
    for key, val in guest_dict.items():
        f.write( '{}:{}\n'.format( key, val ) )
    f.close()
    return guest_dict


def set_event(): #Добавление мероприятия. Аналогично добавлению организатора
    case3 = Event
    case3.event_type = input_numbers( case3.event_type, case3.event_type_label.__str__() )
    case3.date = input_date( case3.date_label.__str__() )
    case3.duration = input_number("Введите длительность мероприятия(в минутах)")
    key = case3.date
    value = case3.event_type
    event_dict.update( {key: value} )
    f = open( 'events.txt', 'ab' )
    pickle.dump(event_dict,f)
    # for key, val in event_dict.items():
    #     f.write( '{}:{}\n'.format( key, val ) )
    f.close()
    return case3.duration


def set_dishes(): #добавление блюд. Пользовательский ввод не предусмотрен
    dish.append( Dishes( 'Фаршированный цыпленок', 200, {'Белки': 50, 'Жиры': 35, 'Углеводы': 70, 'Каллорийность': 480}, 250 ) )
    dish.append( Dishes( 'Свиная отбивная', 200, {'Белки': 30, 'Жиры': 75, 'Углеводы': 60, 'Каллорийность': 430}, 350 ) )
    dish.append( Dishes( 'Запеченая рыба в сливках', 250, {'Белки': 40, 'Жиры': 65, 'Углеводы': 70, 'Каллорийность': 370}, 420 ) )
    dish.append( Dishes( 'Шарлотка', 150, {'Белки': 30, 'Жиры': 70, 'Углеводы': 90, 'Каллорийность': 350}, 230 ) )
    dish.append( Dishes( 'Семифредо', 150, {'Белки': 20, 'Жиры': 60, 'Углеводы': 80, 'Каллорийность': 330}, 280 ) )
    return dish


def set_drinks(): #добавление напитков. Пользовательский ввод не предусмотрен
    drink.append( Drinks( 'Сок', 200, Drinks.alcohol[2], 100 ) )
    drink.append( Drinks( 'Молочный коктейль', 250, Drinks.alcohol[2], 150 ) )
    drink.append( Drinks( 'Газированные напитки', 200, Drinks.alcohol[2], 130 ) )
    drink.append( Drinks( 'Виски', 50, Drinks.alcohol[1], 150 ) )
    drink.append( Drinks( 'Вино', 150, Drinks.alcohol[1], 180 ) )
    drink.append( Drinks( 'Водка', 50, Drinks.alcohol[1], 150 ) )
    return drink


def set_entertaiment(): #добавление развлечений. Пользовательский ввод не предусмотрен
    entertaiment.append( Entertaiment( 'Караоке', 4, Entertaiment.inventory[3], 300, Entertaiment.activity[1] ) )
    entertaiment.append( Entertaiment( 'Дискотека', 15, Entertaiment.inventory[2], 400, Entertaiment.activity[2] ) )
    entertaiment.append( Entertaiment( 'Подвижные конкурсы', 6, Entertaiment.inventory[2], 200, Entertaiment.activity[3] ) )
    entertaiment.append( Entertaiment( 'Творческие конкурсы', 8, Entertaiment.inventory[2], 200, Entertaiment.activity[1] ) )
    return entertaiment

def set_place(): #добавление мест проведения. Пользовательский ввод не предусмотрен
    place.append(Place(20, 8000, Place.design[1], 160, "Лиговский проспект, дом 50"))
    place.append(Place(18, 7000, Place.design[3], 100, "Невский проспект, дом 18"))
    place.append(Place(14, 5000, Place.design[4], 110, "1я Красноармейская ул. дом 16"))
    place.append(Place(10, 4000, Place.design[3], 85, "Коломяжский пр. дом 20"))
    place.append(Place(12, 6000, Place.design[2], 90, "Думская ул. дом 4"))
    return place

def set_count(): #функция подсчета напитков, блюд, развлечений и гостей
    for i in range(len(drink)):
        count.drinks[drink[i].name] = 0
    for i in range(len(dish)):
        count.dishes[dish[i].name] = 0
    for i in range(len(entertaiment)):
        count.entertaiments[entertaiment[i].name] = 0
    count.guests['Студент'] = 0
    count.guests['Школьник'] = 0
    count.guests['Начинающий работник'] = 0
    count.guests['Работник со стажем'] = 0
    count.guests['Пенсионер'] = 0
    return count #фактически возвращается экземпляр класса с нулевыми значениями для дальнейшего подсчета в процессе моделирования


def get_organisator_ratio(): #считаем "успешность" Организатора
    org_ratio = {}
    i=1
    for item in org.keys():
        level = 0
        for key in org[item]:
            if key == 'Temper':
                level = level + int( org[item][key] )
            if key == 'Education':
                level = level + int( org[item][key] )
            if key == 'Portfolio':
                level = level + int( org[item][key] )
            org_ratio[item] = level
    return org_ratio

def get_enjoing_drink(guest,drink):
        enjoy=0
        if guest['Social_status'] == '1':
            if drink.alcohol == 'Да':
                enjoy=enjoy+1
            if drink.price > 150:
                enjoy=enjoy+1
        if guest['Social_status'] == '2':
            if drink.volume > 150:
                enjoy = enjoy + 1
        if guest['Social_status'] == '3':
            if drink.alcohol == 'Да':
                enjoy=enjoy+1
            if drink.price > 100:
                enjoy=enjoy+1
        if guest['Social_status'] == '4':
            if drink.alcohol == 'Да':
                enjoy=enjoy+1
        if guest['Social_status'] == '5':
            if drink.alcohol == 'Да':
                enjoy=enjoy+1
            if drink.price < 150:
                enjoy=enjoy+1
        return enjoy

def get_enjoing_dish(guest,dish):
        enjoy=0
        if guest['Social_status'] == '1':
            if dish.weight > 10:
                enjoy=enjoy+1
            if dish.price > 100:
                enjoy=enjoy+1
        if guest['Social_status'] == '2':
            if dish.weight > 150:
                enjoy = enjoy + 1
        if guest['Social_status'] == '3':
            if dish.price > 250:
                enjoy=enjoy+1
        if guest['Social_status'] == '4':
            if dish.consistency['Жиры']> 50:
                enjoy=enjoy+1
        if guest['Social_status'] == '5':
            if dish.weight < 160:
                enjoy=enjoy+1
            if dish.consistency['Каллорийность'] < 350:
                enjoy=enjoy+1
        return enjoy

def get_enjoing_entertaiment(guest,entertaiment):
    enjoy = 0
    if guest['Social_status'] == '1':
       if entertaiment.activity == 'Маленькая физическая активность':
           enjoy = enjoy +1
       if entertaiment.activity == 'Средняя физическая активность':
           enjoy = enjoy +2
       if entertaiment.activity == 'Высокая физическая активность':
           enjoy = enjoy +4

    if guest['Social_status'] == '2':
        if entertaiment.activity == 'Маленькая физическая активность':
            enjoy = enjoy + 2
        if entertaiment.activity == 'Средняя физическая активность':
            enjoy = enjoy + 2
        if entertaiment.activity == 'Высокая физическая активность':
            enjoy = enjoy + 5

    if guest['Social_status'] == '3':
        if entertaiment.activity == 'Маленькая физическая активность':
            enjoy = enjoy
        if entertaiment.activity == 'Средняя физическая активность':
            enjoy = enjoy + 2
        if entertaiment.activity == 'Высокая физическая активность':
            enjoy = enjoy

    if guest['Social_status'] == '4':
        if entertaiment.activity == 'Маленькая физическая активность':
            enjoy = enjoy +1
        if entertaiment.activity == 'Средняя физическая активность':
            enjoy = enjoy +2
        if entertaiment.activity == 'Высокая физическая активность':
            enjoy = enjoy

    if guest['Social_status'] == '5':
        if entertaiment.activity == 'Маленькая физическая активность':
            enjoy = enjoy + 4
        if entertaiment.activity == 'Средняя физическая активность':
            enjoy = enjoy + 1
        if entertaiment.activity == 'Высокая физическая активность':
            enjoy = enjoy - 1
    return enjoy













