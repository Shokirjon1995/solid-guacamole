names = ['Ivan', 'Pavel', 'Jordan']
print(names[-2])
print(names[1][2])

Black_list = ['Ford', 'Tesla', 'Chervrolet', 'Kia', 'BMW']
print(Black_list[:2])


names = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names.append(11)
print(names)
names.insert(0,0)
print(names)
names.extend([12, 13, 14, 15])
print(names)

# Operator in
Black_list = ['Ford', 'Tesla', 'Chervrolet', 'Kia', 'BMW']
if 'Audi' in Black_list:
    print("Есть такая машина в списке")
else:
    print("Нет такой машины")


# Primer

name = input('Введите слово ')
names.clear()
names.extend(name)
print(names)
