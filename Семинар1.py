#Напишите программу, которая запрашивает год и проверяет его на високосность.
#Распишите все возможные проверки в цепочке elif
#Откажитесь от магических чисел
#Обязательно учтите год ввода Григорианского календаря
#В коде должны быть один input и один print

def Task1():
    year = int(input('введите год'))
    result = None
    if year % 4 != 0:
        result = 'Обычный'
    elif year % 100 == 0:
        if year % 400 == 0:
            result = 'Высокосный'
        else:
            result = 'Обычный'
    else:
        result = 'Высокосный'
    print(result)
    
#Task1()
    
#Пользователь вводит число от 1 до 999. Используя операции с числами
#сообщите что введено: цифра, двузначное число или трёхзначное число.
#Для цифры верните её квадрат, например 5 - 25
#Для двузначного числа произведение цифр, например 30 - 0
#Для трёхзначного числа его зеркальное отображение, например 520 - 25
#Если число не из диапазона, запросите новое число
#Откажитесь от магических чисел
#В коде должны быть один input и один print
    

def Task2():
    MAX_NUMBER = 1000
    MIN_NUMBER = 0
    TENS = 10
    HUNDREDS = 100
    THOUTHENDS = 1000

    while True:
        number = int(input('Введите число от 1 до 999; '))
        if MIN_NUMBER < number < MAX_NUMBER:
            if number < TENS:   
                result = number**2
            elif number < HUNDREDS:
                result = (number // TENS) * (number % TENS)
            else:
                result = (
                    number % TENS * HUNDREDS + number // TENS % TENS * TENS + number // HUNDREDS
                )
            break    
    print(result)    

#Task2()
    

# Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
    #Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********


def Task3():
     height = int(input('Введите высоту елки: '))
     for i in range(height):
         print(f'{"*" * (2 * i + 1):^{2 * height + 1}}')
     
     
#Task3()
         

# Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

def Task4():
    for k in (0,4):
        print("\n")
        for i in range(2, 11):
            print("")
            for j in range(2+k, 6+k):
                print(f"{j} * {i} = {i * j} \t", end=" ")

Task3()



# print('\n\n'.join(['\n'.join(['\t\t'.join([f'{y:<2}* {x:<2} = {x*y:>2}' for y in range(2+n,6+n)]) for x in range(2,11)]) for n in (0,4)])) Вармант решения задачи 3 в одну строку