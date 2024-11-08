import json
import yfinance as yf
import openai

class NewsController():
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
        prompt = f"Get me the most relevant link for the specified symbol that has the highest chance of influencing the price: {symbol} . Chose from here: {news}"
        openai.api_key = ''
        responce = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role": "user", "content": prompt}
            ]
        )
        message = responce['choices'][0]['message']['content']
        print(message)


def main():
    controller = NewsController(["AAPL", "TSLA", "AMZN"])
    #.get_relevant_link("AAPL", controller.get_symbol_news("AAPL"))
    print(controller.get_two_highest_value(["AAPL", "TSLA", "GOOGL"]))

if __name__ == "__main__":
    main()