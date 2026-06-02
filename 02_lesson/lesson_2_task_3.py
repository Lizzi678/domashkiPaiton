import math
def square(side):
    area = side * side
    result = math.ceil(area)
    return result
print(square(2.5))

#import math - подключает интсрументы для работы с математикой
#area = side * side - вычисленние площади по формуле
#def square(side) - объявление функции, которая принимает сторону side
#math.ceil(area) - функция выполняет округление
#return result - выдает результат наружу