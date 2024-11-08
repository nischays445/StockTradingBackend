
# Portfolio and Investment Management System Documentation

This Python-based investment management system leverages MongoDB as the database for managing portfolios and investments. The core functionality revolves around creating and managing portfolios, adding investments to those portfolios, and performing various operations such as updating and deleting investments and portfolios.

## Key Concepts

### Portfolio
- A portfolio is a collection of investments.
- Each portfolio has a unique ID (returned upon creation) that is crucial for accessing and modifying the portfolio.
- You can add, update, or delete portfolios. Portfolios hold investments by their investment IDs.

### Investment
- An investment represents a financial asset, such as a stock.
- Each investment has a unique ID, returned when it is created. Once added to a portfolio, the investment ID can be retrieved directly from the portfolio.

### MongoDB Collections
- `portfolios`: Stores portfolio data with fields like name and investments.
- `investments`: Stores investment data with fields such as `symbol`, `quantity`, `purchase_price`, and `portfolio`.

## Methods Overview

### Portfolio Management
- `add_portfolio(name, investments=None)`: Creates a new portfolio and returns its ID.
- `get_portfolio(id)`: Retrieves a portfolio's details using its ID.
- `delete_portfolio(id)`: Deletes a portfolio by its ID.
- `update_portfolio(id, name=None, investments=None)`: Updates a portfolio's name or adds new investments to it.
- `get_all_portfolio_ids()`: Retrieves all portfolio IDs.
- `get_investment_ids_for_portfolio(portfolio_id)`: Retrieves investment IDs for a given portfolio.

### Investment Management
- `add_investment(symbol, name, quantity, purchase_price, purchase_date, portfolio)`: Creates a new investment, links it to a portfolio, and returns the investment ID.
- `get_investment(id)`: Retrieves an investment's details using its ID.
- `delete_investment(id)`: Deletes an investment by its ID.
- `update_investment(id, name=None, quantity=None, purchase_price=None, purchase_date=None)`: Updates investment details like name, quantity, or purchase price.

### Helper Methods
- `add_investment_to_portfolio(id, investment_id)`: Adds an investment to a portfolio by updating the portfolio with the investment ID.
- `get_collection(collection_name)`: Retrieves all documents from a specific MongoDB collection.

## Example Usage

### Initializing the Database

```python
from your_module import Database

db = Database()
```

### Creating a Portfolio
You can create a portfolio by providing its name and, optionally, an initial list of investment IDs:

```python
portfolio_id = db.add_portfolio("Tech Stocks")
print(f"New portfolio created with ID: {portfolio_id}")
```

### Adding an Investment
To add a new investment, pass the required details like symbol, name, quantity, purchase price, and date:

```python
investment_id = db.add_investment("AAPL", "Apple Inc.", 10, 150, "2023-09-01", "Tech Stocks")
print(f"New investment created with ID: {investment_id}")
```

### Adding Investment to Portfolio
Once the investment has been created, you can add it to a portfolio using its ID:

```python
db.add_investment_to_portfolio(portfolio_id, investment_id)
print(f"Added investment {investment_id} to portfolio {portfolio_id}")
```

### Retrieving a Portfolio
To get the details of a portfolio:

```python
portfolio = db.get_portfolio(portfolio_id)
print(portfolio)
```

### Updating a Portfolio
You can update a portfolio's name or add new investments:

```python
db.update_portfolio(portfolio_id, name="Updated Portfolio Name")
```

### Retrieving All Portfolios
To get the list of all portfolio IDs:

```python
all_portfolio_ids = db.get_all_portfolio_ids()
print(all_portfolio_ids)
```

### Retrieving Investments in a Portfolio
To fetch all the investments within a portfolio:

```python
investment_ids = db.get_investment_ids_for_portfolio(portfolio_id)
print(investment_ids)
```

## Notes
- **Portfolio ID is crucial**: Once you create a portfolio, the ID must be used to access and manage it.
- **Investment ID can be retrieved from the portfolio**: Once an investment is added to a portfolio, you can forget its individual ID and retrieve it directly from the portfolio.
- The system supports CRUD operations on both portfolios and investments.
- This setup provides a flexible and scalable way to manage investments within portfolios, allowing for real-time updates, additions, and retrievals from the database.
