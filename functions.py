from models import *
import json
import re

org = {}
guest_dict = {}
event_dict = {}
drink = []
dish = []
entertaiment=[]
f1 = open( "organisators.txt", 'r' )
f3 = open( "guests.txt", 'r' )
for i in f1.readlines():
    key, val = i.strip().split( ':', maxsplit=1 )
    org[key] = val
for i in f3.readlines():
    key, val = i.strip().split( ':', maxsplit=1 )
    guest_dict[key] = val
f1.close()
f3.close()


def input_numbers(dictionary, label):
    while True:
        print( label )
        for i in range( len( dictionary ) ):
            print( "{} - {}".format( i + 1, dictionary[i + 1] ) )
        x = input( "Введите вариант" )
        try:
            x = int( x )
        except ValueError:
            print( "Это не число. Пожалуйста, введите число, соответствующее номеру варианта " )
            continue

        if x > 0 and x < len( dictionary ) + 1:
            return int( x )
            break
        else:
            print( "Введите число, соответсвующее номеру варианта" )


def input_number(param):
    print( param )
    while True:
        x = input( "Введите целое число" )
        try:
            x = int( x )
        except ValueError:
            print( "Это не целое число. Пожалуйста, введите число" )
            continue
        return x


def input_date(label):
    while True:
        print( label )
        date = input( "Введите дату в формате dd-mm-gggg " )
        result = re.findall( r'\d{2}[-./:]\d{2}[-./:]\d{4}', date )
        if result == []:
            print( "Введите дату в корректном формате" )
        else:
            day, month, year = re.split( r'[-./:]', result[0], maxsplit=2 )
            if (0 < int( day ) < 32) and (0 < int( month ) < 13) and (2017 < int( year ) < 2099):
                return "{}.{}.{}".format( day, month, year )
                break
            else:
                print( "Такой даты не существует, или запись на данную дату невозможна" )


def input_mutch(dictionary):
    out_dict = {}
    number = input_number( "Количество людей" )
    for i in range( number ):
        add = input_numbers( dictionary, 'Выбор' )
        for key, val in dictionary:
            out_dict[add] = val
        dictionary.pop( add )
    return out_dict, number


def set_organisator():
    case1 = Organisator( input_numbers( Organisator.amount ), 0 )
    if case1.amount == 2:
        case1.numbers = input_number( case1.numbers_label.__str__() )
    for i in range( case1.numbers ):
        key = input( "Введите имя" )
        value = {'Education': input_numbers( Person.education, Person.education_label.__str__() ),
                 'Portfolio': input_numbers( Person.portfolio, Person.portfolio_label.__str__() ),
                 'Age': input_number( Person.age_label.__str__() ),
                 'Appearance': input_numbers( Person.appearance, Person.appearance_label.__str__() ),
                 'Sex': input_numbers( Person.sex, Person.sex_label.__str__() ),
                 'Speciality': input_numbers( Person.speciality, Person.speciality_label.__str__() ),
                 'Temper': input_numbers( Person.temper, Person.temper_label.__str__() ),
                 'Budget': input_number( Person.budget_label.__str__() )}

        org.update( {key: value} )
        # value.clear()
    f = open( 'organisators.txt', 'a' )
    for key, val in org.items():
        f.write( '{}:{}\n'.format( key, val ) )
    f.close()


def get_names(dictionary):
    names = {}
    i = 1
    for item in dictionary.keys():
        names[i] = item
        i += 1
    return names


def set_guest():
    case2 = Guest
    case2.amount = input_number( case2.amount_label.__str__() )
    for i in range( case2.amount ):
        key = input( "Введите имя" )
        value = {'Temper': input_numbers( Human.temper, Human.temper_label.__str__() ),
                 'Social_status': input_numbers( Human.social_status, Human.social_status_label.__str__() ),
                 'Age': input_number( Human.age_label.__str__() ),
                 'Sex': input_numbers( Human.sex, Human.sex_label.__str__() )}
        guest_dict.update( {key: value} )
    f = open( 'guests.txt', 'a' )
    for key, val in guest_dict.items():
        f.write( '{}:{}\n'.format( key, val ) )
    f.close()
    return guest_dict


def set_event():
    case3 = Event
    case3.event_type = input_numbers( case3.event_type, case3.event_type_label.__str__() )
    case3.date = input_date( case3.date_label.__str__() )
    key = case3.date
    value = case3.event_type
    event_dict.update( {key: value} )
    f = open( 'events.txt', 'a' )
    for key, val in event_dict.items():
        f.write( '{}:{}\n'.format( key, val ) )
    f.close()
    return event_dict


def set_dishes():
    dish.append( Dishes( 'Фаршированный цыпленок', 200, {'Белки': 50, 'Жиры': 35, 'Углеводы': 70, 'Каллорийность': 480}, 250 ) )
    dish.append( Dishes( 'Свиная отбивная', 200, {'Белки': 30, 'Жиры': 75, 'Углеводы': 60, 'Каллорийность': 430}, 350 ) )
    dish.append( Dishes( 'Запеченая рыба в сливках', 250, {'Белки': 40, 'Жиры': 65, 'Углеводы': 70, 'Каллорийность': 370}, 420 ) )
    dish.append( Dishes( 'Шарлотка', 150, {'Белки': 30, 'Жиры': 70, 'Углеводы': 90, 'Каллорийность': 350}, 230 ) )
    dish.append( Dishes( 'Семифредо', 150, {'Белки': 20, 'Жиры': 60, 'Углеводы': 80, 'Каллорийность': 330}, 280 ) )
    return dish


def set_drinks():
    drink.append( Drinks( 'Сок', 200, Drinks.alcohol[2], 100 ) )
    drink.append( Drinks( 'Молочный коктейль', 250, Drinks.alcohol[2], 150 ) )
    drink.append( Drinks( 'Газированные напитки', 200, Drinks.alcohol[2], 130 ) )
    drink.append( Drinks( 'Виски', 50, Drinks.alcohol[1], 150 ) )
    drink.append( Drinks( 'Вино', 150, Drinks.alcohol[1], 180 ) )
    drink.append( Drinks( 'Водка', 50, Drinks.alcohol[1], 150 ) )
    return drink


def set_entertaiment():
    entertaiment.append( Entertaiment( 'Караоке', 4, Entertaiment.inventory[3], 300, Entertaiment.activity[1] ) )
    entertaiment.append( Entertaiment( 'Дискотека', 15, Entertaiment.inventory[2], 400, Entertaiment.activity[2] ) )
    entertaiment.append( Entertaiment( 'Подвижные конкурсы', 6, Entertaiment.inventory[2], 200, Entertaiment.activity[3] ) )
    entertaiment.append( Entertaiment( 'Творческие конкурсы', 8, Entertaiment.inventory[2], 200, Entertaiment.activity[1] ) )
    return entertaiment



def get_organisator_ratio():
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










