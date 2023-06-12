rate = input("Оцените работу оператора от 1 до 5")
rate_num = int(rate)
if (rate_num < 1):
    rate_num = 1

if (rate_num > 5):
    rate_num = 5

feedback = ''

if rate_num == 1:
    feedback = input("расскажите, что нам улучшить: ")
elif rate_num == 2:
    feedback = input("расскажите, что вам не понравилось: ")
elif rate_num == 3:
    feedback = input("расскажите, что как нам стать лучше: ")
elif rate_num == 4:
    feedback = input("расскажите, что добавить: ")
else:
    feedback = input("спасибо, за хорошую оценку: ")

print(feedback)
