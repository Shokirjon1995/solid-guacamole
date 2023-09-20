# 1 урок
#First_number = int(input('Введите первое число '))
#Second_number = int(input('Введите второе число '))
#Znak_math = input('Введите математическую операцию ')
#if Znak_math == '+':
#    print('Операция сложение',f'{First_number} + {Second_number} = {First_number + Second_number}')
#elif Znak_math == '-':
#    print('Операция отнимание', f'{First_number} - {Second_number} = {First_number - Second_number}')
#elif Znak_math == '*':
#    print('Операция умножение', f'{First_number} * {Second_number} = {First_number * Second_number}')
#else:
#    print('Операция деление', f'{First_number} / {Second_number} = {First_number / Second_number}')

import random

first_player = input('Сделайте выбор — камень, ножницы или бумага: ')
possible_actions = ["камень", "бумага", "ножницы"]
computer_action = random.choice(possible_actions)
print(f"\nВы выбрали {first_player}, компьютер выбрал {computer_action}.\n")
if first_player == computer_action:
    print(f"Оба пользователя выбрали {first_player}. Ничья!!")
elif first_player == "камень":
    if computer_action == "ножницы":
        print("Камень бьет ножницы! Вы победили!")
    else:
        print("Бумага оборачивает камень! Вы проиграли.")
elif first_player == "бумага":
    if computer_action == "камень":
        print("Бумага оборачивает камень! Вы победили!")
    else:
        print("Ножницы режут бумагу! Вы проиграли.")
elif first_player == "ножницы":
    if computer_action == "бумага":
        print("Ножницы режут бумагу! Вы победили!")
    else:
        print("Камень бьет ножницы! Вы проиграли.")


