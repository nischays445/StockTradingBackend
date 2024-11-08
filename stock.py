from models.investment import Investment

class Stock(Investment):
    def __init__(self, stock_id=None, stock_symbol="", stock_name="", stock_quantity=0, stock_purchase_price=0.0, stock_purchase_date="", stock_value=0.0, stock_current_price=0.0, stock_unrealized_gains_losses=0.0, stock_dividend_income=0.0, stock_sector="", stock_marketcap=0.0, stock_earnings_per_share=0.0):
        super().__init__(stock_id, "stock", stock_symbol, stock_name, stock_quantity, stock_purchase_price, stock_purchase_date, stock_value, stock_current_price, stock_unrealized_gains_losses)
        self.dividend_income = stock_dividend_income
        self.sector = stock_sector
        self.marketcap = stock_marketcap
        self.earnings_per_share = stock_earnings_per_share
    # Conventional getters and setters for dividend_income
    @property
    def dividend_income(self):
        return self._dividend_income

    @dividend_income.setter
    def dividend_income(self, value):
        self._dividend_income = value

    # Conventional getters and setters for sector
    @property
    def sector(self):
        return self._sector

    @sector.setter
    def sector(self, value):
        self._sector = value

    # Conventional getters and setters for marketcap
    @property
    def marketcap(self):
        return self._marketcap

    @marketcap.setter
    def marketcap(self, value):
        self._marketcap = value

    # Conventional getters and setters for earnings_per_share
    @property
    def earnings_per_share(self):
        return self._earnings_per_share

    @earnings_per_share.setter
    def earnings_per_share(self, value):
        self._earnings_per_share = value
