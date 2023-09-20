all_products = {'Склад':{'name':'Хлеб', 'количество': 34}}

def get_product(a = 'name'):
    print(all_products['Склад'][a])

get_product('name')

def spam1(*args):
    return args

print(spam1(1,2,3,'hello'))

def spammer(*args):
    for a in args:
        print(a)
spammer(1,2,3,1,2,3,4,'Hello')


def spam1(**kwargs):
    for k in kwargs.items():
        for v in kwargs.items():
            return k, v

print(spam1(name = 'my1', age = 23))