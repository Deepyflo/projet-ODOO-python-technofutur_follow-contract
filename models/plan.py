class Plan:
    def __init__(self, id, name, price, quota):
        self._id = id
        self.name = name
        self.price = price
        self.quota = quota

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def quota(self):
        return self._quota

    @quota.setter
    def quota(self, value):
        self._quota = value