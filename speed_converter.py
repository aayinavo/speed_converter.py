speed = float(input("Введите скорость в километрах в час: "))

mps = speed / 3.6
mph = speed / 1.609

print("Скорость в метрах в секунду: ", round(mps, 2))
print("Скорость в милях в час: ", round(mph, 2))
