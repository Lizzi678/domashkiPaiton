from smartphone import Smartphone

# Наполняем каталог пятью экземплярами класса
catalog = [
    Smartphone("Apple", "iPhone 15", "+79001112233"),
    Smartphone("Samsung", "Galaxy S23", "+79004445566"),
    Smartphone("Xiaomi", "Redmi Note 12", "+79007778899"),
    Smartphone("Google", "Pixel 8", "+79000001122"),
    Smartphone("Huawei", "P60", "+79003334455")
]

# Цикл для печати каталога в нужном формате
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")