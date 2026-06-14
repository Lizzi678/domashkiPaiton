from address import Address
from mailing import Mailing

# Создаем экземпляры адресов
address_from = Address("101000", "Москва", "ул. Ленина", "10", "5")
address_to = Address("190000", "Санкт-Петербург", "пр. Невский", "1", "12")

# Создаем экземпляр почтового отправления
parcel = Mailing(address_to, address_from, 350, "RU123456789")

# Выводим информацию в требуемом формате
print(f"Отправление {parcel.track} из "
      f"{parcel.from_address.index}, {parcel.from_address.city}, "
      f"{parcel.from_address.street}, {parcel.from_address.house} - {parcel.from_address.apartment} "
      f"в {parcel.to_address.index}, {parcel.to_address.city}, "
      f"{parcel.to_address.street}, {parcel.to_address.house} - {parcel.to_address.apartment}. "
      f"Стоимость {parcel.cost} рублей.")