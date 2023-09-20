name = []
number = []
service = []


while True:
    sentense = input("Введите что вы хотите добавить, Имя, Номер, Сервис ")
    if sentense == 'Имя':
        a = input("Добавьте имя ")
        name.append(a)
        print(name)
    elif sentense =="Номер":
        b = input("Добавьте номер ")
        number.append(b)
        print(number)
    else:
        c = input("Введите услугу ")
        service.append(c)
        print(service)

