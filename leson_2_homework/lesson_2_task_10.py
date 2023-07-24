def bank(X, Y):
    for each_year in range(Y):
        X = (X * 1.1)
    return X

X = int(input("Сумма вклада?"))
Y = int(input("На сколько лет?"))

print(bank(X, Y))

