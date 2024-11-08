from db.database import Database
from bson import ObjectId


class Investment:
    def __init__(self, investment_id=None, investment_type="", investment_symbol="", investment_name="", investment_quantity=0, investment_purchase_price=0.0, investment_purchase_date="", investment_value=0.0, investment_unrealized_gains_losses=0.0):
        self.id = investment_id if investment_id else str(ObjectId())
        self.type = investment_type
        self.symbol = investment_symbol
        self.name = investment_name
        self.quantity = investment_quantity
        self.purchase_price = investment_purchase_price
        self.purchase_date = investment_purchase_date
        self.value = investment_value
        self.unrealized_gains_losses = investment_unrealized_gains_losses

    def calculate_unrealized_gains_losses(self):
        self.unrealized_gains_losses = (self.current_price - self.purchase_price) * self.quantity

    def update_value(self):
        self.value = self.current_price * self.quantity
    # Conventional Getters and Setters
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def symbol(self):
        return self._symbol

    @symbol.setter
    def symbol(self, value):
        self._symbol = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def purchase_price(self):
        return self._purchase_price

    @purchase_price.setter
    def purchase_price(self, value):
        self._purchase_price = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def unrealized_gains_losses(self):
        return self._unrealized_gains_losses

    @unrealized_gains_losses.setter
    def unrealized_gains_losses(self, value):
        self._unrealized_gains_losses = value
