all_products = {'Весь склад':{'Sok': 10 , 'Nestle': 10}}
cart =[]
while True:
    admin = int(input("Что вы хотите сделать? 1-Добавить в склад  2 - Добавить в корзину  3 - показать весь список склада  4- Остановить "))
    if admin == 1:
        product_name = input('Что вы хотите добавить? ')
        product_count = input('Введите количество: ')
        all_products['Весь склад'][product_name] = product_count
        print("Продукт успешно добавлен")
    elif admin == 2:
        print(all_products)
        product = input("Что из перечисленного в складе хотите добавить в корзину? ")

        if product in all_products['Весь склад'].keys():
            product_co = int(input("Введите количество "))
            all_products['Весь склад'][product] -= product_co
            order = (product, product_co)
            cart.append(order)
            print()

        else:
            print(all_products.values())
            print("Введите правильно количество")

    elif admin == 3:
        print(all_products)
    elif admin == 4:
        break
    else:
        print("Неправильное занчение")