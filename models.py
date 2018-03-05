from datetime import datetime


class Organisator():
    amount_label = "Огранизатор"
    amount={1 :"Физическое лицо",
            2 : "Юридическое лицо"}
    numbers_label="Введите количество организаторов"

    numbers=0

    def __init__(self, amount, numbers = 0):
        self.amount = amount
        self.numbers = numbers


class Person(Organisator):
    education_label = "Образование"
    education={1 : "Профильное высшее",
               2 : "Непрофильное высшее",
               3 : "Курсы",
               4 : "Отсутствует"}
    portfolio_label = "Портфолио"
    portfolio={1 : "Более 50 проведенных мероприятий",
               2 : "От 20 до 50 проведенных мероприятий",
               3 : "От 1 до 20 проведенных мероприятий",
               4 : "Впервые организовывает праздник"}
    temper_label = "Характер"
    temper={1 : "Дружелюбный",
            2 : "Агрессивный",
            3 : "Равнодушный"}
    age_label = "Возраст организатора"
    age=0

    sex={1 : "Мужчина",
         2 : "Женщина"}
    sex_label = "Пол"
    speciality={1 : "Новый Год",
                2 : "День Рождения",
                3 : "Семейная вечеринка",
                4 : "Корпоратив"}
    speciality_label = "Специализация"
    appearance={1 : "Располагающая",
                2 : "Отталкивающая"}
    appearance_label = "Внешность"
    budget=0
    budget_label = "Предполагаемый бюджет"
    def __init__(self, education, portfolio, temper, age, sex, speciality, appearance, budget):
        self.budget = budget
        self.temper = temper
        self.speciality = speciality
        self.sex = sex
        self.age = age
        self.portfolio = portfolio
        self.appearance = appearance
        self.education = education





class Guest():
    amount=0
    amount_label = "Количество гостей"

    def __init__(self, amount):
        self.amount = amount


class Human(Guest):
    age=0
    age_label = "Возраст"
    sex = {1 : "Мужчина",
           2 : "Женщина"}
    sex_label = "Пол"
    social_status={1 : "Студент",
                   2 : "Школьник",
                   3 : "Начинающий работник",
                   4 : "Работник со стажем",
                   5 : "Пенсионер"}
    social_status_label = "Социальный статус"
    temper = {1: "Дружелюбный",
              2: "Агрессивный",
              3: "Равнодушный"}
    temper_label = "Характер"

    def __init__(self,age,sex,social_status,temper):
        self.age = age
        self.sex = sex
        self.social_status = social_status
        self.temper = temper

class Event():
    event_type={1 : "Новый Год",
                2 : "День Рождения",
                3 : "Хэллоуин",
                4 : "23 Февраля",
                5 : "8 марта",
                6 : "9 мая",
                7 : "1 сентября",
                8 : "День России",
                9 : "Другое"}
    event_type_label = "Праздник"
    date=0
    date_label = "Дата праздника"

class Place():
    capacity=0
    capacity_label = "Вместимость места проведения"
    address=""
    address_label = "Адрес"
    square=0
    square_label = "Площадь помещения"
    design={1 : "Восточный",
            2 : "Западный",
            3 : "Скандинавский",
            4 : "Детский"}
    design_label = "Дизайн интерьера"
    price=0
    price_label = "цена"

    def __str__(self):
        return "Место проведения"

class Dishes():
    name=""
    name_label = "Название"
    consistency={}
    consistency_label = "Состав"
    weight=0
    weight_label = "Вес"
    price=0
    price_label = "цена"

    def __init__(self, name, consistency, weight, price):
        self.name = name
        self.price = price
        self.consistency = consistency
        self.weight = weight

    def __str__(self):
        return "Блюда"



class Drinks():
    name=""
    name_label = "Название"
    alcohol={1 : "Да",
             2 : "Нет"}
    alcohol_label = "Содержит алкоголь"
    volume=0
    volume_label = "Объем"
    price=0
    price_label = "Цена"

    def __init__(self, name, volume, alcohol, price):
        self.name = name
        self.volume = volume
        self.price = price
        self.alcohol = alcohol

    def __str__(self):
        return "Напитки"


class Entertaiment():
    name=""
    name_label = "Название"
    capacity=0
    capacity_label = "Количество участников"
    duration=0
    duration_label = "продолжительность"
    inventory={1 : "Не нужен",
               2 : "Небольшое количество",
               3 : "Большое количество"}
    inventory_label = "Инвентарь"
    activity = {1 : "Маленькая физическая активность",
                2 : "Средняя физическая активность",
                3 : "Высокая физическая активность"}

    def __init__(self, name, capacity, duration, inventory,activity):
        self.name = name
        self.capacity = capacity
        self.duration = duration
        self.inventory = inventory
        self.activity = activity

    def __str__(self):
        return "Конкурсы и развлечения"



