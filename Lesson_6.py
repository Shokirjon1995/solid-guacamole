data = {'name': ['Jordan', 'Pavel'], 'age':(12,21), 'jobs': 'programmers'}

if 'name' in data:
    print('Da')
else:
    print('net')

users ={}
users['name'] = 'Jordan'
print(users)

my_dict = {'song':'Godzilla', 'singer':'Eminem'}
#my_dict.clear()
#my_dict.pop('song')
my_dict.popitem()
print(my_dict)



my = ['2', '33', '33', 2, 'TgBot']
my2 = set(my)
print(my2)




instructor = dict(name = 'Jordan', age = 32, job = 'Python developer')

for k in instructor.keys():
    print(k)
for v in instructor.values():
    print(v)
for k, v in instructor.items():
    print(k,v)



prazdniki = {'Navruz':'21 Marta', 'Noviy god': '31 dekabrya'}
day = input("Kakoy prazdnik? ")

print(prazdniki.get(day))

