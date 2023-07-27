def bank(x, y):
    for each_year in range(y):
        x = round(x * 1.1)
    return round(x, 2)

x = int(input("Сумма вклада? "))
y = int(input("На сколько лет? "))

print("Вы получите: ", bank(x, y))

