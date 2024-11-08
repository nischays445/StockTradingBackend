from models.investment import Investment

class Crypto(Investment):
    def __init__(self, crypto_id=None, crypto_symbol="", crypto_name="", crypto_quantity=0, crypto_purchase_price=0.0, crypto_purchase_date="", crypto_value=0.0, crypto_current_price=0.0, crypto_unrealized_gains_losses=0.0, circulating_supply=0.0):
        super().__init__(crypto_id, "crypto", crypto_symbol, crypto_name, crypto_quantity, crypto_purchase_price, crypto_purchase_date, crypto_value, crypto_current_price, crypto_unrealized_gains_losses)
        self.circulating_supply = circulating_supply
    #Conventional Getters and Setters
    @property
    def circulating_supply(self):
        return self.circulating_supply
    @circulating_supply.setter
    def circulating_supply(self, value):
        self.circulating_supply = value
