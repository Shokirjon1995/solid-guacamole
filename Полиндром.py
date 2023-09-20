while True:
    sentense = input("Введите предложение: ")
    if sentense == sentense[::-1]:
        print("Да полиндром!")
    else:
        print("Увы не полиндром!!.")

