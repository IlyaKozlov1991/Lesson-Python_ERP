import easygui
from easygui import *  
import print_log
from print_log import viev_log

def menu(): # Создает интерфейс меню
    global type_vvod
    type_vvod = ()
    msg = "Что делать будем?"
    title = "Меню"
    choices = ["Посчитаем простое числе", "Посчитаем комплексное число", \
        "Посмотрим логи", "Бежим отсюда!"]
    output = choicebox(msg, title, choices)
    if output == "Посчитаем простое числе":
        type_vvod = "Простое число"
        vvod()
    elif output == "Посчитаем комплексное число":
        type_vvod = "Комплексное число"
        vvod()
    elif output == "Посмотрим логи":
        viev_log()
    elif output == "Бежим отсюда!":
        exit()
    
def vvod(): # Создает интерфейс окна ввода уравнения
    global var1                 # Переменная куда будем записывать данные.
    msg = "Введите уравнение"   # Сообщение
    title = "Ввод уравнения"    # Шапочка.
    fieldNames = ["Уравнение"]  # Ввод уравнения
    fieldValues = []  
    fieldValues = multenterbox(msg,title, fieldNames)
    var1 = fieldValues[0]       # Запись уравнения в переменную (строка)

def transform_vvod(): # 
    global var_l
    var_l = list(var1)
    n = 0
    for n in range(len(var_l)):
        if var_l[n] == "1" or var_l[n] == "2" or var_l[n] == "3" or var_l[n] == "4" \
            or var_l[n] == "5" or var_l[n] == "6" or var_l[n] == "7" or var_l[n] == "8" \
                or var_l[n] == "9" or var_l[n] == "0":
                    i = int(var_l[n])
                    var_l[n] = i

    if var_l[0] == "-":
        var_l.pop(0)
        var_l[0] = var_l[0] * -1
    elif var_l[0] == "+":
        var_l.pop(0)
    
    n = 0
    for n in range(len(var_l)): 
        if var_l[n] == "(" or var_l[n] == "+" or var_l[n] == "-" or var_l[n] == "/" \
             or var_l[n] == "*":
                if var_l[n + 1] == "-":
                    var_l[n+2] = var_l[n+2] * -1
                    var_l[n+1] = ""
                elif var_l[n+1] == " " and var_l[n+2] == "-":
                    var_l[n+3] = var_l[n+3] * -1
                    var_l[n+2] = ""

def clean_vvod():
    n = 0
    global var_2
    var_2 = []
    for n in range(len(var_l)):
        if var_l[n] != " " and var_l[n] != "(" and var_l[n] != ")":
            var_2.append(var_l[n])

def goin_vvod():
    global var_3
    global var_4
    var_3 = []
    var_4 = []
    n = 0
    f = str()
    for n in range(len(var_2)):
        if type(var_2[n]) == int:
            f = f + str(var_2[n])
        else:
            var_3.append(f)
            var_3.append(var_2[n])
            f = str()
    var_3.append(f)
    for n in range(len(var_3)):
        if var_3[n] != "":
            var_4.append(var_3[n])

def fin_var():
    global var_fin
    var_fin = []
    n = 0
    for n in range(len(var_4)):
        if var_4[n] == "+" or var_4[n] == "-" or var_4[n] == "/" or var_4[n] == "*" \
            or var_4[n] == "i" or var_4[n] == "j":
            var_fin.append(var_4[n])
        else:
            h = int(var_4[n])
            var_fin.append(h)

def start_menu():
    menu()
    transform_vvod()
    clean_vvod() 
    goin_vvod()
    fin_var()

start_menu()
print(type_vvod)
print(var1)
# print(var_l)
# print(var_2)
# print(var_4)
print(var_fin)

