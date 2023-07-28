from user import User
from card import Card

user_1 = User('Юлия')

user_1.say_name()
user_1.set_age(33)
user_1.say_age()

card = Card("1233 4355 2456 5678", "09/29", "Julia")

user_1.add_card(card)
user_1.get_card().pay(1000)