import datetime
import json
import yfinance as yf
import pandas_market_calendars as mcal

class main_controller:
    def __init__(self):
        print(f"{main_controller.get_current_time()}: Backend has Started")


    @classmethod
    def get_current_time(cls):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time


    @classmethod
    def get_oneday_data(cls, symbol):
        print(f"{cls.get_current_time()}: Getting one day data for '{symbol}'")
        day = datetime.datetime.today().date()
        ticker = yf.Ticker(symbol)
        count = 0
        hist = 0
        while True:
            try:
                print(f"{cls.get_current_time()}: Getting data from Yahoo Finance API")
                hist = ticker.history(interval="1m", start=day, end=day + datetime.timedelta(days=1), prepost=True)
                print(f"{cls.get_current_time()}: Attemping to restrucure API Output content")
                hist.reset_index(inplace=True)
                hist['Datetime'] = hist['Datetime'].apply(lambda x: x.isoformat())
            except KeyError as e:
                print(f"{cls.get_current_time()}: No data found for {day}. Trying previous day")
                day = day - datetime.timedelta(days=1)
                count = count + 1
                if count == 10:
                    break
                continue
            break
        if count == 10:
            print(f"{cls.get_current_time()}: Checked previous 10 days for '{symbol}'. No results, maybe delisted? ")
            return
        json_data = hist.to_json(orient='records', date_format='iso')
        data_dict = json.loads(json_data)
        formatted_json = json.dumps(data_dict, indent=4)
        print(f"{cls.get_current_time()}: API Content has been structured")
        print(f"{cls.get_current_time()}: Writing to JSON")
        with open("oneday_data.json", "w") as f:
            f.write(formatted_json)
        print(f"{cls.get_current_time()}: Data has been saved to oneday_data.json")


    @classmethod
    def get_fiveday_data(cls, symbol):
        print(f"{cls.get_current_time()}: Checking if '{symbol}' is active")
        if cls.is_symbol_active(symbol) == False:
            print(f"{cls.get_current_time()}: '{symbol}' is not active. No data to fetch")
            return
        print(f"{cls.get_current_time()}: Getting five day data for '{symbol}'")
        today = datetime.datetime.today().date()
        start_date = today - datetime.timedelta(days=5)
        ticker = yf.Ticker(symbol)
        print(f"{cls.get_current_time()}: Getting data from Yahoo Finance API")
        hist = ticker.history(interval="30m", start=start_date, end=today + datetime.timedelta(days=1), prepost=True)
        print(f"{cls.get_current_time()}: Attemping to Structure API Output")
        hist.reset_index(inplace=True)
        hist['Datetime'] = hist['Datetime'].apply(lambda x: x.isoformat())
        json_data = hist.to_json(orient='records', date_format='iso')
        data_dict = json.loads(json_data)
        formatted_json = json.dumps(data_dict, indent=4)
        print(f"{cls.get_current_time()}: API Content has been structured")
        print(f"{cls.get_current_time()}: Writing to JSON")
        with open("fiveday_data.json", "w") as f:
            f.write(formatted_json)
        print(f"{cls.get_current_time()}: Data has been saved to fiveday_data.json")


    @classmethod
    def get_onemonth_data(cls, symbol):
        print(f"{cls.get_current_time()}: Checking if '{symbol}' is active")
        if cls.is_symbol_active(symbol) == False:
            print(f"{cls.get_current_time()}: '{symbol}' is not active. No data to fetch")
            return
        print(f"{cls.get_current_time()}: Getting one month data for '{symbol}'")
        today = datetime.datetime.today().date()
        start_date = today - datetime.timedelta(days=30)
        ticker = yf.Ticker(symbol)
        print(f"{cls.get_current_time()}: Getting data from Yahoo Finance API")
        hist = ticker.history(interval="1d", start=start_date, end=today + datetime.timedelta(days=1))
        print(f"{cls.get_current_time()}: Attemping to Structure API Output")
        hist.reset_index(inplace=True)
        hist['Date'] = hist['Date'].apply(lambda x: x.isoformat())
        json_data = hist.to_json(orient='records', date_format='iso')
        data_dict = json.loads(json_data)
        formatted_json = json.dumps(data_dict, indent=4)
        print(f"{cls.get_current_time()}: API Content has been structured")
        print(f"{cls.get_current_time()}: Writing to JSON")
        with open("onemonth_data.json", "w") as f:
            f.write(formatted_json)
        print(f"{cls.get_current_time()}: Data has been saved to onemonth_data.json")


    @classmethod
    def get_oneyear_data(cls, symbol):
        print(f"{cls.get_current_time()}: Checking if '{symbol}' is active")
        if cls.is_symbol_active(symbol) == False:
            print(f"{cls.get_current_time()}: '{symbol}' is not active. No data to fetch")
            return
        print(f"{cls.get_current_time()}: Getting one year data for '{symbol}'")
        today = datetime.datetime.today().date()
        start_date = today - datetime.timedelta(days=365)
        ticker = yf.Ticker(symbol)
        print(f"{cls.get_current_time()}: Getting data from Yahoo Finance API")
        hist = ticker.history(interval="1d", start=start_date, end=today + datetime.timedelta(days=1))
        print(f"{cls.get_current_time()}: Attemping to Structure API Output")
        hist.reset_index(inplace=True)
        hist['Date'] = hist['Date'].apply(lambda x: x.isoformat())
        json_data = hist.to_json(orient='records', date_format='iso')
        data_dict = json.loads(json_data)
        formatted_json = json.dumps(data_dict, indent=4)
        print(f"{cls.get_current_time()}: API Content has been structured")
        print(f"{cls.get_current_time()}: Writing to JSON")
        with open("oneyear_data.json", "w") as f:
            f.write(formatted_json)
        print(f"{cls.get_current_time()}: Data has been saved to oneyear_data.json")


    @classmethod
    def get_historical_data(cls,symbol, first_date, last_date):
        print(f"{cls.get_current_time()}: Checking if '{symbol}' is active")
        if cls.is_symbol_active(symbol) == False:
            print(f"{cls.get_current_time()}: '{symbol}' is not active. No data to fetch")
            return
        print(f"{cls.get_current_time()}: Getting Historical stock data between {first_date} and {last_date} for '{symbol}'")
        start_date = datetime.datetime.strptime(first_date, '%Y-%m-%d')
        end_date = datetime.datetime.strptime(last_date, '%Y-%m-%d')
        print(f"{cls.get_current_time()}: Getting data from Yahoo Finance API")
        investment_data = yf.download(symbol, start=start_date, end=end_date, prepost= True)
        print(f"{cls.get_current_time()}: Attemping to Strcture API Output")
        investment_data.reset_index(inplace=True)
        investment_data['Date'] = investment_data['Date'].apply(lambda x: x.isoformat())
        json_data = investment_data.to_json(orient='records', date_format='iso')
        data_dict = json.loads(json_data)
        formatted_json = json.dumps(data_dict, indent=4)
        print(f"{cls.get_current_time()}: API Content has been structured")
        print(f"{cls.get_current_time()}: Writing to JSON")
        with open("historical_data.json", "w") as f:
            f.write(formatted_json)
        print(f"{cls.get_current_time()}: Data has been saved to historical_data.json")


    @classmethod
    def get_investment_info(cls, symbol):
        print(f"{cls.get_current_time()}: Checking if '{symbol}' is active")
        if cls.is_symbol_active(symbol) == False:
            print(f"{cls.get_current_time()}: '{symbol}' is not active. No data to fetch")
            return
        ticker = yf.Ticker(symbol)
        print(f"{cls.get_current_time()}: Getting data from Yahoo Finance API")
        investment_data = ticker.info
        print(f"{cls.get_current_time()}: Getting Current Price Info")
        current_price = ticker.fast_info['lastPrice']
        print(f"{cls.get_current_time()}: Attemping to Structure API Output")
        investment_data['currentPrice'] = current_price
        formatted_json = json.dumps(investment_data, indent=1)
        print(f"{cls.get_current_time()}: API Content has been structured")
        print(f"{cls.get_current_time()}: Writing to JSON")
        with open("investment_data.json", "w") as f:
            f.write(formatted_json)
        print(f"{cls.get_current_time()}: Data has been saved to investment_data.json")


    @classmethod
    def is_symbol_active(cls, symbol):
        if symbol[-3::] == "USD":
            print(f"Checking if '{symbol}' is active")
            ticker = yf.Ticker(symbol)
            try:
                print(f"{cls.get_current_time()}: Getting data from Yahoo Finance API")
                info = ticker.info
                if 'volume' not in info:
                    print(f"'{cls.get_current_time()}: {symbol}' is not active or delisted")
                    return False
                elif info['volume'] == 0 or info['volume'] == None:
                    print(f"{cls.get_current_time()}: '{symbol}' is not active or delisted")
                    return False
                else:
                    print(f"{cls.get_current_time()}: '{symbol}' is active")
                    return True
            except Exception as e:
                print(f"{cls.get_current_time()}: Error checking status for '{symbol}': {e}")
                return False
        else:
            day = datetime.datetime.today().date()
            nyse = mcal.get_calendar('NYSE')
            nasdaq = mcal.get_calendar('NASDAQ')
            nyse_holidays = nyse.holidays().holidays
            nasdaq_holidays = nasdaq.holidays().holidays
            while True:
                day = day - datetime.timedelta(days=1)
                if day.weekday() >=5:
                    day = day- datetime.timedelta(days=1)
                elif day in nyse_holidays:
                    day = day- datetime.timedelta(days=1)
                elif day in nasdaq_holidays:
                    day = day- datetime.timedelta(days=1)
                else:
                    break
            print(f"Checking if '{symbol}' is active")
            ticker = yf.Ticker(symbol)
            try:
                print(f"{cls.get_current_time()}: Getting data from Yahoo Finance API")
                info = ticker.history(interval="1m", start=day, end=day + datetime.timedelta(days=1), prepost=True)
                if info.empty:
                    print("Stock is not active or delisted")
                    return False
                else:
                    print("Stock is active")
                    return True
            except Exception as e:
                print(f"Error checking stock status for '{symbol}': {e}")
                return False


def main():
    #Testing Functions
    controller = main_controller()
    symbol = input("Fetch Data for symbol: ")
    choice = int(input("Enter choice for checking. 1) oneday data 2) fiveday data 3) onemonth data 4) oneyear data 5) historical data 6) investment info 7) is symbol active: "))
    if choice == 1:
        controller.get_oneday_data(symbol)
    elif choice == 2:
        controller.get_fiveday_data(symbol)
    elif choice == 3:
        controller.get_onemonth_data(symbol)
    elif choice == 4:
        controller.get_oneyear_data(symbol)
    elif choice == 5:
        first_date = input("Enter Start Date (YYYY-MM-DD): ")
        last_date = input("Enter End Date (YYYY-MM-DD): ")
        controller.get_historical_data(symbol, first_date, last_date)
    elif choice == 6:
        controller.get_investment_info(symbol)
    elif choice == 7:
        controller.is_symbol_active(symbol)


if __name__ == "__main__":
    main()
