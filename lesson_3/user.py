class User:
    age = 0;
    
    def __init__(self, name):
        print("Я создался")
        self.user_name = name

    def say_name(self):
        print('Меня зовут: ', self.user_name)

    def say_age(self):
        print(self.age)

    def set_age(self, new_age):
        self.age = new_age

    def add_card(self, card):
        self.card = card

    def get_card(self):
        return self.card
    