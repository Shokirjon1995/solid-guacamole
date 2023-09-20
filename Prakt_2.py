class User:
    def __init__ (self, name, post, age, phone_number):
        self.name = name
        self.post = post
        self.age = age
        self.phone_number = phone_number

    def change_name(self, username):
        self.name = username

    def change_post(self, new_post):
        self.post = new_post

    def change_number(self, phone):
        self.phone_number = phone

user1 = User('Eshmat','aa@gmmail.com',23 , 998998999999)
print(user1.name, user1.post, user1.age,user1.phone_number)
