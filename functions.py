from models import *
org=[]
def input_numbers(dictionary):
    while True:
        for i in range( len( dictionary ) ):
            print( "{} - {}".format( i + 1, dictionary[i + 1] ) )
        x = input( "Введите вариант" )
        try:
            x = int(x)
        except ValueError:
            print( "Это не число. Пожалуйста, введите число, соответствующее номеру варианта " )
            continue

        if x > 0 and x < len( dictionary ):
            return int( x )
            break
        else:
                print( "Введите число, соответсвующее номеру варианта" )

def input_number():
    while True:
        x = input( "Введите целое число" )
        try:
            x = int( x )
        except ValueError:
            print( "Это не целое число. Пожалуйста, введите число" )
            continue
        return x

def get_organisator():
    f=open("organisators.txt", 'a')
    case1 = Organisator(input_numbers(Organisator.amount), 0)
    value=[]
    if case1.amount == 2:
        print("Введите количество организаторов")
        case1.numbers=input_number()
    for i in range(case1):
        value.append(Person(input_numbers(Person.education),
                        input_numbers(Person.portfolio),
                        input_numbers(Person.age),
                        input_numbers(Person.appearance),
                        input_numbers(Person.sex),
                        input_numbers(Person.speciality),
                        input_numbers(Person.temper),
                        input_numbers(Person.budget)))

        org.update({input("Введите имя"), value})
        value=[]
    f.write(org)
    f.close()



