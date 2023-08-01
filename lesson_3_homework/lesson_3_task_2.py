from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Apple", "iPhone 12", "+79123236759")
phone2 = Smartphone("Samsung", "Galaxy S", "+79154567890")
phone3 = Smartphone("Xiaomi", "Mi 11", "+79345678901")
phone4 = Smartphone("Google", "Pixel 5", "+79456078912")
phone5 = Smartphone("OnePlus", "9 Pro", "+79567980123")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")


