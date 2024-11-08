import datetime
import json
import yfinance as yf
import os
class PostMarketReport:
    def __init__(self):
        pass

    @classmethod
    def get_current_time(cls):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        return formatted_time

    @classmethod
    def get_dow_change(cls):
        current_time = datetime.datetime.now().time()
        five_pm = datetime.time(17, 0, 0)
        if current_time < five_pm:
            print("Before 5pm, not running")
            return
        hist = yf.download("^DJI", period="5d")
        hist = hist.to_dict("list")
        closes = hist['Close']
        close_yesterday = closes[-2]
        close_today = closes[-1]
        points_change = close_today - close_yesterday
        percent_change = ((close_today - close_yesterday) / close_yesterday) * 100
        return round(float(points_change), 2), round(float(percent_change), 2)


    @classmethod
    def get_nyse_change(cls):
        current_time = datetime.datetime.now().time()
        five_pm = datetime.time(17, 0, 0)
        if current_time < five_pm:
            print("Before 5pm, not running")
            return
        hist = yf.download("^NYA", period="5d")
        hist = hist.to_dict("list")
        closes = hist['Close']
        close_yesterday = closes[-2]
        close_today = closes[-1]
        points_change = close_today - close_yesterday
        percent_change = ((close_today - close_yesterday) / close_yesterday) * 100
        return round(float(points_change), 2), round(float(percent_change), 2)

    @classmethod
    def get_sp500_change(cls):
        current_time = datetime.datetime.now().time()
        five_pm = datetime.time(17, 0, 0)
        if current_time < five_pm:
            print("Before 5pm, not running")
            return
        hist = yf.download("^GSPC", period="5d")
        hist = hist.to_dict("list")
        closes = hist['Close']
        close_yesterday = closes[-2]
        close_today = closes[-1]
        points_change = close_today - close_yesterday
        percent_change = ((close_today - close_yesterday) / close_yesterday) * 100
        return round(float(points_change), 2), round(float(percent_change), 2)
    @classmethod
    def get_nasdaq_change(cls):
        current_time = datetime.datetime.now().time()
        five_pm = datetime.time(17, 0, 0)
        if current_time < five_pm:
            print("Before 5pm, not running")
            return
        hist = yf.download("^IXIC", period="5d")
        hist = hist.to_dict("list")
        closes = hist['Close']
        close_yesterday = closes[-2]
        close_today = closes[-1]
        points_change = close_today - close_yesterday
        percent_change = ((close_today - close_yesterday) / close_yesterday) * 100
        return round(float(points_change), 2), round(float(percent_change), 2)

    @classmethod
    def get_russell_change(cls):
        current_time = datetime.datetime.now().time()
        five_pm = datetime.time(17, 0, 0)
        if current_time < five_pm:
            print("Before 5pm, not running")
            return
        hist = yf.download("^RUT", period="5d")
        hist = hist.to_dict("list")
        closes = hist['Close']
        close_yesterday = closes[-2]
        close_today = closes[-1]
        points_change = close_today - close_yesterday
        percent_change = ((close_today - close_yesterday) / close_yesterday) * 100
        return round(float(points_change), 2), round(float(percent_change), 2)




    @classmethod
    def get_combined_market_report(cls):
        current_time = datetime.datetime.now().time()
        five_pm = datetime.time(17, 0, 0)
        if current_time < five_pm:
            print("Before 5pm, not running")
            return
        dow_price, dow_percentage = cls.get_dow_change()
        nyse_price, nyse_percentage = cls.get_nyse_change()
        sp500_price, sp500_percentage = cls.get_sp500_change()
        nasdaq_price, nasdaq_percentage = cls.get_nasdaq_change()
        russel_price, russel_percentage = cls.get_russell_change()

        market_report = {
            "Dow Jones": {
                "price_change": dow_price,
                "percentage_change": dow_percentage
            },
            "NYSE": {
                "price_change": nyse_price,
                "percentage_change": nyse_percentage
            },
            "S&P 500": {
                "price_change": sp500_price,
                "percentage_change": sp500_percentage
            },
            "NASDAQ": {
                "price_change": nasdaq_price,
                "percentage_change": nasdaq_percentage
            },
            "Russell 2000": {
                "price_change": russel_price,
                "percentage_change": russel_percentage
            },
        }
        os.makedirs("report_info", exist_ok=True)
        with open(os.path.join("report_info", "report_info.json"), "w") as f:
            f.write(json.dumps(market_report, indent=4))

        return market_report

def main():
    controller = PostMarketReport()
    market_report = controller.get_combined_market_report()
    current_time = controller.get_current_time()
    print(f"{current_time} - Market Overview Written to {datetime.date.today()}_market_overview.json")

if __name__ == "__main__":
    main()