import backtrader as bt
from datetime import datetime
import yfinance as yf
import pandas as pd
from strategies.macd_strategy import MACDStrategy

def run_backtest(symbol='EURUSD=X', 
                start_date='2024-01-01',
                end_date='2025-02-15',
                initial_cash=100000):
    """
    Führt Backtest mit der Advanced Multi-Indicator Strategie durch
    """
    
    # Daten herunterladen
    print(f'Lade Daten für {symbol}...')
    data = yf.download(symbol, start=start_date, end=end_date)
    
    # Cerebro erstellen
    cerebro = bt.Cerebro()
    
    # Daten hinzufügen
    feed = bt.feeds.PandasData(dataname=data)
    cerebro.adddata(feed)
    
    # Strategie hinzufügen
    cerebro.addstrategy(MACDStrategy)
    
    # Startkapital setzen
    cerebro.broker.setcash(initial_cash)
    
    # Kommission setzen (0.1%)
    cerebro.broker.setcommission(commission=0.001)
    
    # Analysen hinzufügen
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
    cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
    
    print('Startkapital: %.2f' % cerebro.broker.getvalue())
    
    # Backtest ausführen
    results = cerebro.run()
    strat = results[0]
    
    # Ergebnisse ausgeben
    final_value = cerebro.broker.getvalue()
    profit = final_value - initial_cash
    drawdown = strat.analyzers.drawdown.get_analysis()['max']['drawdown']
    losses = strat.analyzers.trades.get_analysis()['losers']
    wins = strat.analyzers.trades.get_analysis()['wins']
    win_rate = wins / (wins + losses) if (wins + losses) > 0 else 0

    print('Endkapital: %.2f' % final_value)
    print('Profit: %.2f' % profit)
    print('Max Drawdown: %.2f' % drawdown)
    print('Losses: %d' % losses)
    print('Wins: %d' % wins)
    print('Win Rate: %.2f%%' % (win_rate * 100))
    print('Sharpe Ratio:', strat.analyzers.sharpe.get_analysis())
    print('Max Drawdown: %.2f%%' % drawdown)
    print('Anzahl Trades:', strat.analyzers.trades.get_analysis()['total']['total'])
    if strat.analyzers.trades.get_analysis()['total']['total'] > 0:
        print('Gewinnende Trades: %.2f%%' % 
              (strat.analyzers.trades.get_analysis()['won']['total'] / strat.analyzers.trades.get_analysis()['total']['total'] * 100))
    
    # Analysen ausgeben
    sharpe_ratio = strat.analyzers.sharpe.get_analysis()
    drawdown = strat.analyzers.drawdown.get_analysis()
    trades = strat.analyzers.trades.get_analysis()
    print('\nPerformance Analyse:')
    print('Sharpe Ratio:', sharpe_ratio['sharperatio'])
    print('Max Drawdown: %.2f%%' % drawdown['max']['drawdown'])
    print('Anzahl Trades:', trades['total']['total'])
    if trades['total']['total'] > 0:
        print('Gewinnende Trades: %.2f%%' % 
              (trades['won']['total'] / trades['total']['total'] * 100))
    print('\nDetaillierte Ergebnisse:')
    print('Endkapital: %.2f' % final_value)
    print('Profit: %.2f' % profit)
    print('Max Drawdown: %.2f' % drawdown)
    print('Losses: %d' % losses)
    print('Wins: %d' % wins)
    print('Win Rate: %.2f%%' % (win_rate * 100))
    print('Sharpe Ratio:', sharpe_ratio['sharperatio'])
    print('Max Drawdown: %.2f%%' % drawdown['max']['drawdown'])
    print('Anzahl Trades:', trades['total']['total'])
    if trades['total']['total'] > 0:
        print('Gewinnende Trades: %.2f%%' % 
              (trades['won']['total'] / trades['total']['total'] * 100))
    
    # Plot erstellen
    cerebro.plot(style='candlestick')
