from pymongo import MongoClient
from bson.objectid import ObjectId
import certifi


class Database:
    def __init__(self, db_name='investment_manager'):
        self.client = MongoClient('mongodb+srv://user:password@cluster0.hl9ha.mongodb.net', tlsCAFile=certifi.where())

        self.db = self.client[db_name]
        self.portfolios = self.db.portfolios
        self.investments = self.db.investments

    def get_portfolio(self, id):
        portfolio_id = ObjectId(id)
        return self.portfolios.find_one(portfolio_id)

    def get_investment(self, id):
        investment_id = ObjectId(id)
        return self.investments.find_one(investment_id)

    def add_portfolio(self, name, investments=None):
        if investments is None:
            investments = []
        new_portfolio = {"name": name, "investments": investments}
        portfolio_id = self.portfolios.insert_one(new_portfolio).inserted_id
        return portfolio_id

    def delete_portfolio(self, id):
        portfolio_id = ObjectId(id)
        result = self.portfolios.delete_one({"_id":portfolio_id})
        print(f"Deleted {result.deleted_count} documents")

    def update_portfolio(self, id, name=None, investments=None):
        update = {"$set": {}}
        if name is not None:
            update["$set"]["name"] = name
        if investments is not None:
            existing_portfolio = self.get_portfolio(id)
            if existing_portfolio and "investments" in existing_portfolio and len(
                    existing_portfolio["investments"]) > 0:
                existing_investments = existing_portfolio["investments"][0]
                updated_investments = existing_investments + "," + investments
                update["$set"]["investments.0"] = updated_investments
            else:
                update["$set"]["investments.0"] = investments
        print(update)
        portfolio_id = ObjectId(id)
        result = self.portfolios.update_one(
            {"_id": portfolio_id},
            update
        )
        print(f"Matched {result.matched_count} document(s).")
        print(f"Modified {result.modified_count} document(s).")
        return self.portfolios.find_one(portfolio_id)

    def add_investment(self, symbol, name, quantity, purchase_price, purchase_date,  portfolio):
        new_stock = {"name": name, "symbol": symbol, "quantity" : quantity, "purchase_price": purchase_price, "purchase_date": purchase_date, "portfolio": portfolio}
        return self.investments.insert_one(new_stock).inserted_id

    def delete_investment(self, id):
        investment_id = ObjectId(id)
        result = self.investments.delete_one({"_id": investment_id})
        return f"Deleted {result.deleted_count} doucments"

    def update_investment(self, id, name=None, quantity=None, purcahse_price= None, purchase_date= None):
        print(id)
        print(name)
        update = {"$set": {}}
        if name is not None:
            update["$set"]["name"] = name
        if quantity is not None:
            update["$set"]["quantity"] = quantity
        if purcahse_price is not None:
            update["$set"]["purcahse_price"] = purcahse_price
        if purchase_date is not None:
            update["$set"]["purchase_date"] = purchase_date
        investment_id = ObjectId(id)

        result = self.investments.update_one(
            {"_id": investment_id},
            update
        )

        print(f"Matched {result.matched_count} document(s).")
        print(f"Modified {result.modified_count} document(s).")
        return(self.investments.find_one(investment_id))

    def get_collection(self, collection_name):
        collection = self.db.get_collection(collection_name)
        return list(collection.find())

    def update_portfolio_name(self, id, name):

        self.update_portfolio(id, name)
        return

    def update_investment_name(self, id, name):
        self.update_investment(id, name)
        return

    def update_investment_quantity(self, id, quantity):
        self.update_investment(id, None, quantity)

    def update_investment_purchase_price(self, id, purchase_price):
        self.update_investment(id, None, purchase_price)
        return
    def update_investment_purchase_date(self, id, purchase_date):
        self.update_investment( id, None, None, purchase_date)
        return

    def get_portfolio_name(self, id):
        portfolio = self.get_portfolio(id)
        return portfolio['name']

    def get_investment_name(self, id):
        investment = self.get_investment(id)
        return investment['name']

    def get_investment_quantity(self, id):
        investment = self.get_investment(id)
        return investment['quantity']

    def get_investment_purchase_price(self, id):
        investment = self.get_investment(id)
        return investment['purchase_price']

    def get_investment_purchase_date(self, id):
        investment = self.get_investment(id)
        return investment['purchase_date']

    def add_investment_to_portfolio(self, id, investment_id):
        self.update_portfolio(id, None, investment_id)

    def get_all_portfolio_ids(self):
        portfolios = self.portfolios.find({}, {"_id": 1})
        portfolio_ids = [str(portfolio["_id"]) for portfolio in portfolios]
        return portfolio_ids

    def get_investment_ids_for_portfolio(self, portfolio_id):
        portfolio = self.get_portfolio(portfolio_id)
        if portfolio and "investments" in portfolio:
            return portfolio["investments"]
        return []

def main():
    pass
    #db = Database()
    #db.add_portfolio("Random Stocks")
    #db.add_investment_to_portfolio("66eadf79189a65c96614aa06", "66eadc2c03c3c11bef13726e")
if __name__ == "__main__":
    main()
