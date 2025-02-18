import backtrader as bt
from indicator_loader import IndicatorLoader
from datetime import datetime

class IndicatorTester:
    def __init__(self, indicators_dir):
        self.loader = IndicatorLoader(indicators_dir)

    def run_tests(self, data):
        indicators = self.loader.load_indicators()
        results = self.loader.test_indicators(data)
        self.report_results(results)

    def report_results(self, results):
        for indicator, success in results.items():
            print(f'Indicator: {indicator}, Test Successful: {success}')

if __name__ == "__main__":
    cerebro = bt.Cerebro()
    data1 = bt.feeds.YahooFinanceData(dataname='AAPL', fromdate=datetime(2024, 1, 1), todate=datetime(2024, 1, 31))
    data2 = bt.feeds.YahooFinanceData(dataname='GOOG', fromdate=datetime(2024, 1, 1), todate=datetime(2024, 1, 31))
    cerebro.adddata(data1)
    cerebro.adddata(data2)
    tester = IndicatorTester('Indikatoren')
    tester.run_tests(data1)
    tester.run_tests(data2)
