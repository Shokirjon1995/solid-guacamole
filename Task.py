list_1 = ['Audi', 'Chevrolet', 'BMW']
print(list_1)
delete = "Удалить"
edit = "Изменить"
add = "Добавить"
a = input(f'Какое условие хотите сделать {delete}, {edit}, {add} ')
if a == delete:
    list_1.clear()
    print(list_1)
elif a == edit:
    x = input('Какой элемент нужно изменить?')
    i = list_1.index(x)
    list_1[i] = 'Tesla'
    print(list_1)
elif a == add:
    b = input("Что хотите добавить? ")
    list_1.append(b)
    print(list_1)
else:
    print("Error 404 Not found")