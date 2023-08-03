class Address:
    def __init__(self, index, city, street, house, flat):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def print_index(self):
        print(self.index)

    def print_city(self):
        print(self.city)

    def print_street(self):
        print(self.street)

    def print_house(self):
        print(self.house)

    def print_flat(self):
        print(self.flat)

