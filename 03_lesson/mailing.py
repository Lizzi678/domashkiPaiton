from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address   # Объект класса Address
        self.from_address = from_address # Объект класса Address
        self.cost = cost
        self.track = track