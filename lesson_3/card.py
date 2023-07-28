class Card:
    number = '0000 0000 0000 0000'
    valid_date = '09/29'
    holedr = 'unknow'

    def __init__(self, number, date, holder):
        self.number = number
        self.valid_date = date
        self.holedr = holder

    def pay(self, amount):
        print("С карты ", self.number, "списали ", amount)
