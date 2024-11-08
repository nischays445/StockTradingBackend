# `main_controller` Class

## `__init__(self)`
Initializes the `main_controller` class and prints a message indicating that the backend has started.

## `get_current_time(cls)`
Returns the current date and time as a formatted string.

## `get_oneday_data(cls, symbol)`
Fetches one day of historical data for the given symbol from Yahoo Finance and saves it to `oneday_data.json`.

**Parameters:**
- `symbol` (`str`): The symbol to fetch data for.

## `get_fiveday_data(cls, symbol)`
Fetches five days of historical data for the given symbol from Yahoo Finance and saves it to `fiveday_data.json`.

**Parameters:**
- `symbol` (`str`): The symbol to fetch data for.

## `get_onemonth_data(cls, symbol)`
Fetches one month of historical data for the given symbol from Yahoo Finance and saves it to `onemonth_data.json`.

**Parameters:**
- `symbol` (`str`): The symbol to fetch data for.

## `get_oneyear_data(cls, symbol)`
Fetches one year of historical data for the given symbol from Yahoo Finance and saves it to `oneyear_data.json`.

**Parameters:**
- `symbol` (`str`): The symbol to fetch data for.

## `get_historical_data(cls, symbol, first_date, last_date)`
Fetches historical data for the given symbol between the specified dates from Yahoo Finance and saves it to `historical_data.json`.

**Parameters:**
- `symbol` (`str`): The symbol to fetch data for.
- `first_date` (`str`): The start date in the format `YYYY-MM-DD`.
- `last_date` (`str`): The end date in the format `YYYY-MM-DD`.

## `get_investment_info(cls, symbol)`
Fetches investment information for the given symbol from Yahoo Finance and saves it to `investment_data.json`.

**Parameters:**
- `symbol` (`str`): The symbol to fetch data for.

## `is_symbol_active(cls, symbol)`
Checks if the given symbol is active by fetching data from Yahoo Finance.

**Parameters:**
- `symbol` (`str`): The symbol to check.

**Returns:**
- `bool`: `True` if the symbol is active, `False` otherwise.
