# NewsController Documentation

The `NewsController` class is designed to retrieve, process, and analyze news and stock data for a list of given stock symbols. This class uses **Yahoo Finance API** (`yfinance`), and **OpenAI GPT** to fetch relevant news links for the specified stock symbols.

## Requirements

- `yfinance` for fetching stock data.
- `openai` for querying GPT to identify the most relevant news article.

You can install the required libraries with:

```bash
pip install yfinance openai
Class: NewsController
Constructor: __init__(self, symbols)
Initializes the NewsController class with a list of stock symbols.

Parameters:
symbols (List[str]): A list of stock symbols (e.g., ["AAPL", "TSLA", "AMZN"]) to track.
Example:
python
Copy code
controller = NewsController(["AAPL", "TSLA", "AMZN"])
Method: get_symbols_news(self)
Returns the list of news articles for all the symbols.

Returns:
List[dict]: A list of news articles for the tracked symbols.
Example:
python
Copy code
news = controller.get_symbols_news()
Method: get_two_highest_value(self, symbols)
Fetches the two symbols with the highest closing value from a provided list of stock symbols.

Parameters:
symbols (List[str]): A list of stock symbols (e.g., ["AAPL", "TSLA", "GOOGL"]).
Returns:
List[str]: A list of the two symbols with the highest closing values.
Example:
python
Copy code
top_symbols = controller.get_two_highest_value(["AAPL", "TSLA", "GOOGL"])
Method: get_symbol_news(self, symbol)
Fetches news articles for a specific stock symbol.

Parameters:
symbol (str): The stock symbol (e.g., "AAPL").
Returns:
List[dict]: A list of news articles related to the given stock symbol.
Example:
python
Copy code
news = controller.get_symbol_news("AAPL")
Method: get_relevant_link(self, symbol, news)
Uses OpenAI's GPT-3 to identify the most relevant news link from a list of news articles that could influence the price of the stock symbol.

Parameters:
symbol (str): The stock symbol (e.g., "AAPL").
news (List[dict]): A list of news articles related to the stock symbol.
Returns:
None: Prints the most relevant link based on GPT-3's analysis.
Example:
python
Copy code
controller.get_relevant_link("AAPL", controller.get_symbol_news("AAPL"))
Note: You need to set up your OpenAI API key for this method to work.

Example Usage
python
Copy code
import yfinance as yf
import openai

class NewsController:
    def __init__(self, symbols):
        self.symbols = symbols
        self.news = []

    def get_symbols_news(self):
        return self.news

    def get_two_highest_value(self, symbols):
        gainers = {}
        for symbol in symbols:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1d")
            close = hist['Close']
            gainers[symbol] = close.iloc[0]
        sorted_gainers = sorted(gainers.items(), key=lambda x: x[1], reverse=True)
        return [symbol for symbol, _ in sorted_gainers[:2]]

    def get_symbol_news(self, symbol):
        ticker = yf.Ticker(symbol)
        news = ticker.news
        return news

    def get_relevant_link(self, symbol, news):
        prompt = f"Get me the most relevant link for the specified symbol that has the highest chance of influencing the price: {symbol}. Choose from here: {news}"
        openai.api_key = 'your-api-key'
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        message = response['choices'][0]['message']['content']
        print(message)


def main():
    controller = NewsController(["AAPL", "TSLA", "AMZN"])
    print(controller.get_two_highest_value(["AAPL", "TSLA", "GOOGL"]))

if __name__ == "__main__":
    main()
Notes
Yahoo Finance API (yfinance): This library is used to fetch stock historical data and news for the provided symbols.
OpenAI GPT-3: The get_relevant_link method requires an API key for OpenAI. You need to set your API key for GPT to generate the most relevant news link.
Stock Symbols: Make sure that the stock symbols provided are valid and supported by Yahoo Finance.
License
This project is licensed under the MIT License - see the LICENSE file for details.



