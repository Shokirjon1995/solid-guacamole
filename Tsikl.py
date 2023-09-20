name = 'Pasha'
for item in name:
    print(item)

my_list = [1,'a', 2, 4.65]
for spam in my_list:
    print(spam)
print(f'Всего {len(my_list)} элемента(ов)')

n = [6, 5, '2']

for i in range(1,100):
    print(i)

words =["adopt", "back", "beam", "confide", "grill", "wave"]
past_tense = []
for word in words:
    if word[-1]!= "e":
        past_tense.append(word + "ed")
    else:
        past_tense.append(word + "d")
print(past_tense)


na = ['Ivan', 'Pavel', 'Jordan']
while True:
    new = input('Кого добавим? ')
    na.append(new)
    print(na)

