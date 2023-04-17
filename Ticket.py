total_price = 0
discount = 0.1
quan = input("Введите количество билетов: ")
while isinstance(quan, int) == False:
    try:
        quan = int(quan)
    except:
        quan = input("Введите числовое значение!: ")

for i in range(1, quan+1):
    try:
        age = int(input("Введите возраст "+str(i)+"-го гостя: "))
        if 0 < age <= 100:
            if 18 < age <= 25:
                total_price += 990
            elif age > 25:
                total_price += 1390
        else:
            print("Вам не может быть столько лет!")
    except ValueError as error:
        print("Введите возраст в числовом формате!")

if quan > 3:
    total_price = total_price * (1-discount)

print("Итоговая стоимость:", round(total_price,2), "рублей")