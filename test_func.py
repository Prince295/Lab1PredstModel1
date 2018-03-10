from models import *
import json
import pickle
import re

org = {}
guest_dict = {}
event_dict = {}
drink = []
dish = []
entertaiment=[]
place = []
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


def input_numbers(dictionary, label):
    while True:
        print( label )
        for item in dictionary.keys():
            print( "{} - {}".format( item, dictionary[item] ) )
        x = input( "Введите вариант" )
        try:
            x = int( x )
        except ValueError:
            print( "Это не число. Пожалуйста, введите число, соответствующее номеру варианта " )
            continue

        for item in dictionary.keys():
            if x==item:
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
        for key, val in enumerate(dictionary):
            out_dict[add] = dictionary[add]
        dictionary.pop( add )
    return out_dict, number

def get_names(dictionary):
    names = {}
    i = 1
    for item in dictionary.keys():
        names[i] = item
        i += 1
    return names

def get_organisator_ratio():
    org_ratio = {}
    i=1
    for item in org.keys():
        level = 0
        for key in org[item].keys():
            if key == 'Temper':
                level = level + int( org[item][key] )
            if key == 'Education':
                level = level + int( org[item][key] )
            if key == 'Portfolio':
                level = level + int( org[item][key] )
            org_ratio[item] = level


    return org_ratio


def set_dishes():
    dish.append( Dishes( 'Фаршированный цыпленок', 200, {'Белки': 50, 'Жиры': 35, 'Углеводы': 70, 'Каллорийность': 480}, 250 ) )
    dish.append( Dishes( 'Свиная отбивная', 200, {'Белки': 30, 'Жиры': 75, 'Углеводы': 60, 'Каллорийность': 430}, 350 ) )
    dish.append( Dishes( 'Запеченая рыба в сливках', 250, {'Белки': 40, 'Жиры': 65, 'Углеводы': 70, 'Каллорийность': 370}, 420 ) )
    dish.append( Dishes( 'Шарлотка', 150, {'Белки': 30, 'Жиры': 70, 'Углеводы': 90, 'Каллорийность': 350}, 230 ) )
    dish.append( Dishes( 'Семифредо', 150, {'Белки': 20, 'Жиры': 60, 'Углеводы': 80, 'Каллорийность': 330}, 280 ) )
    return dish

set_dishes()
print(dish[1].consistency)