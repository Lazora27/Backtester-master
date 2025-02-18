import os
import sys
import pandas as pd
import numpy as np
import backtrader as bt
from datetime import datetime, timedelta
import tempfile
import shutil
from scipy import stats
from statsmodels.regression.rolling import RollingOLS
from collections import deque


class ForexStrategy(bt.Strategy):
    """Forex Trading Strategie mit MACD und RSI"""
    
    params = (
        ('macd1', 12),      # Fast EMA
        ('macd2', 26),      # Slow EMA
        ('macd3', 9),       # Signal
        ('rsi_period', 14), # RSI Periode
        ('rsi_upper', 70),  # RSI Überkauft
        ('rsi_lower', 30),  # RSI Überverkauft
        ('stake', 10000),   # Standard Lot Size
        ('printlog', False) # Logging aktivieren
    )
    
    def log(self, txt, dt=None, doprint=False):
        """Logging Funktion"""
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print(f'{dt.isoformat()}, {txt}')
    
    def __init__(self):
        # Daten-Referenzen
        self.dataclose = self.datas[0].close
        self.datahigh = self.datas[0].high
        self.datalow = self.datas[0].low
        self.dataopen = self.datas[0].open
        self.datavolume = self.datas[0].volume
        
        # Order/Position Management
        self.order = None
        self.buyprice = None
        self.buycomm = None
        self.bar_executed = None
        
        # Indikatoren
        self.macd = bt.indicators.MACD(
            self.dataclose,
            period_me1=self.p.macd1,
            period_me2=self.p.macd2,
            period_signal=self.p.macd3)
            
        self.rsi = bt.indicators.RSI(
            self.dataclose,
            period=self.p.rsi_period)
            
        # Für Plotting
        self.macd.plotinfo.plotname = 'MACD'
        self.rsi.plotinfo.plotname = 'RSI'
    
    def notify_order(self, order):
        """Order Status Updates"""
        if order.status in [order.Submitted, order.Accepted]:
            return  # Warte auf weitere Ausführung
            
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    f'BUY EXECUTED, Price: {order.executed.price:.5f}, '
                    f'Cost: {order.executed.value:.2f}, '
                    f'Comm: {order.executed.comm:.2f}')
                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
                
            else:
                self.log(
                    f'SELL EXECUTED, Price: {order.executed.price:.5f}, '
                    f'Cost: {order.executed.value:.2f}, '
                    f'Comm: {order.executed.comm:.2f}')
            
            self.bar_executed = len(self)
            
        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log('Order Canceled/Margin/Rejected')
            
        self.order = None
    
    def notify_trade(self, trade):
        """Trade Status Updates"""
        if not trade.isclosed:
            return
            
        self.log(f'OPERATION PROFIT, GROSS {trade.pnl:.2f}, NET {trade.pnlcomm:.2f}')
    
    def next(self):
        """Nächster Bar"""
        # Ignoriere Perioden ohne Handel
        if self.datavolume[0] == 0:
            return
            
        # Logging
        self.log(f'Close: {self.dataclose[0]:.5f}, RSI: {self.rsi[0]:.2f}')
        
        # Prüfe auf aktive Order
        if self.order:
            return
            
        # Prüfe auf Position im Markt
        if not self.position:
            # Kaufsignal: MACD kreuzt nach oben ODER RSI überverkauft
            if ((self.macd.macd[0] > self.macd.signal[0] and
                 self.macd.macd[-1] <= self.macd.signal[-1]) or
                self.rsi[0] < self.p.rsi_lower):
                
                self.log(f'BUY CREATE {self.dataclose[0]:.5f}')
                self.order = self.buy(size=self.p.stake)
                
        else:
            # Verkaufssignal: MACD kreuzt nach unten ODER RSI überkauft
            if ((self.macd.macd[0] < self.macd.signal[0] and
                 self.macd.macd[-1] >= self.macd.signal[-1]) or
                self.rsi[0] > self.p.rsi_upper):
                
                self.log(f'SELL CREATE {self.dataclose[0]:.5f}')
                self.order = self.sell(size=self.p.stake)
    
    def stop(self):
        """Wird am Ende des Backtests aufgerufen"""
        self.log('End of Period', doprint=True)
        self.log(
            f'Final Portfolio Value: {self.broker.getvalue():.2f}\n'
            f'Final Cash: {self.broker.getcash():.2f}\n'
            f'Final Position Size: {self.position.size if self.position else 0}',
            doprint=True)


class BollingerRSIStrategy(bt.Strategy):
    """Bollinger Bands + RSI Strategie"""
    
    params = (
        ('bb_period', 20),    # Bollinger Periode
        ('bb_dev', 2.0),      # Bollinger Standardabweichungen
        ('rsi_period', 14),   # RSI Periode
        ('rsi_upper', 65),    # RSI Überkauft (aggressiver)
        ('rsi_lower', 35),    # RSI Überverkauft (aggressiver)
        ('stake', 10000),     # Position Size
        ('printlog', False)
    )
    
    def __init__(self):
        self.bb = bt.indicators.BollingerBands(
            self.data.close, period=self.p.bb_period, devfactor=self.p.bb_dev)
        self.rsi = bt.indicators.RSI(
            self.data.close, period=self.p.rsi_period)
        
        # Trend Filter
        self.sma50 = bt.indicators.SMA(self.data.close, period=50)
        
        self.order = None
        self.price_entry = None
    
    def log(self, txt, dt=None, doprint=False):
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print(f'{dt.isoformat()} {txt}')
            
    def next(self):
        if self.order:
            return
            
        if not self.position:
            # Kaufsignal: Preis unter BB + RSI überverkauft + Aufwärtstrend
            if (self.data.close[0] < self.bb.lines.bot[0] and 
                self.rsi[0] < self.p.rsi_lower and
                self.data.close[0] > self.sma50[0]):
                
                self.order = self.buy(size=self.p.stake)
                self.price_entry = self.data.close[0]
        else:
            # Verkaufssignal: Preis über BB oder RSI überkauft oder 0.5% Gewinn
            if (self.data.close[0] > self.bb.lines.top[0] or 
                self.rsi[0] > self.p.rsi_upper or
                self.data.close[0] > self.price_entry * 1.005):
                
                self.order = self.sell(size=self.p.stake)


class ATRStochStrategy(bt.Strategy):
    """ATR + Stochastic Strategie"""
    
    params = (
        ('atr_period', 14),      # ATR Periode
        ('atr_mult', 1.5),       # ATR Multiplikator (aggressiver)
        ('stoch_period', 14),    # Stochastic Periode
        ('stoch_upper', 75),     # Stochastic Überkauft (aggressiver)
        ('stoch_lower', 25),     # Stochastic Überverkauft (aggressiver)
        ('stake', 10000),        # Position Size
        ('printlog', False)
    )
    
    def __init__(self):
        self.atr = bt.indicators.ATR(self.data, period=self.p.atr_period)
        self.stoch = bt.indicators.Stochastic(
            self.data, 
            period=self.p.stoch_period,
            period_dfast=3,      # %D Periode
            period_dslow=3)      # Glättung
        
        # Trend Filter
        self.ema20 = bt.indicators.EMA(self.data.close, period=20)
        
        self.order = None
        self.atr_stop = None
    
    def log(self, txt, dt=None, doprint=False):
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print(f'{dt.isoformat()} {txt}')
            
    def next(self):
        if self.order:
            return
            
        if not self.position:
            # Kaufsignal: Stoch überverkauft + Aufwärtstrend
            if (self.stoch.lines.percK[0] < self.p.stoch_lower and
                self.stoch.lines.percD[0] < self.p.stoch_lower and
                self.data.close[0] > self.ema20[0]):
                
                self.order = self.buy(size=self.p.stake)
                self.atr_stop = self.data.close[0] - self.atr[0] * self.p.atr_mult
        else:
            # Verkaufssignal: Stoch überkauft oder Stop Loss
            if (self.stoch.lines.percK[0] > self.p.stoch_upper or
                self.stoch.lines.percD[0] > self.p.stoch_upper or
                self.data.close[0] < self.atr_stop):
                
                self.order = self.sell(size=self.p.stake)
            else:
                # Update trailing stop
                new_stop = self.data.close[0] - self.atr[0] * self.p.atr_mult
                self.atr_stop = max(self.atr_stop, new_stop)


class EMACCIStrategy(bt.Strategy):
    """EMA Crossover + CCI Strategie"""
    
    params = (
        ('ema_fast', 8),      # Schnelle EMA Periode (aggressiver)
        ('ema_slow', 21),     # Langsame EMA Periode (aggressiver)
        ('cci_period', 20),   # CCI Periode
        ('cci_upper', 75),    # CCI Überkauft (aggressiver)
        ('cci_lower', -75),   # CCI Überverkauft (aggressiver)
        ('stake', 10000),     # Position Size
        ('printlog', False)
    )
    
    def __init__(self):
        self.ema_fast = bt.indicators.EMA(self.data.close, period=self.p.ema_fast)
        self.ema_slow = bt.indicators.EMA(self.data.close, period=self.p.ema_slow)
        self.cci = bt.indicators.CCI(self.data, period=self.p.cci_period)
        
        # Momentum
        self.mom = bt.indicators.MomentumOscillator(self.data.close, period=10)
        
        self.crossover = bt.indicators.CrossOver(self.ema_fast, self.ema_slow)
        self.order = None
    
    def log(self, txt, dt=None, doprint=False):
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print(f'{dt.isoformat()} {txt}')
            
    def next(self):
        if self.order:
            return
            
        if not self.position:
            # Kaufsignal: EMA Crossover + CCI überverkauft + positives Momentum
            if (self.crossover > 0 and 
                self.cci < self.p.cci_lower and
                self.mom > 0):
                
                self.order = self.buy(size=self.p.stake)
        else:
            # Verkaufssignal: EMA Crossover oder CCI überkauft oder negatives Momentum
            if (self.crossover < 0 or 
                self.cci > self.p.cci_upper or
                self.mom < 0):
                
                self.order = self.sell(size=self.p.stake)


class SimpleMAStrategy(bt.Strategy):
    """Eine einfache Moving Average Strategie für Pairs Trading"""
    params = (
        ('fast_period', 5),  # Shorter fast period for more signals
        ('slow_period', 15),  # Shorter slow period
        ('divergence_threshold', 0.0002),  # Minimum price divergence required
        ('printlog', False)
    )
    
    def __init__(self):
        self.order = None
        self.position_size = 1000
        
        # Create moving averages for both assets
        self.fast_ma1 = bt.indicators.SimpleMovingAverage(
            self.data0.close, period=self.params.fast_period)
        self.slow_ma1 = bt.indicators.SimpleMovingAverage(
            self.data0.close, period=self.params.slow_period)
            
        self.fast_ma2 = bt.indicators.SimpleMovingAverage(
            self.data1.close, period=self.params.fast_period)
        self.slow_ma2 = bt.indicators.SimpleMovingAverage(
            self.data1.close, period=self.params.slow_period)
            
        # Create crossover signals
        self.crossover1 = bt.indicators.CrossOver(self.fast_ma1, self.slow_ma1)
        self.crossover2 = bt.indicators.CrossOver(self.fast_ma2, self.slow_ma2)
        
        # Calculate price divergence
        self.divergence = self.data0.close - self.data1.close
        
        # Track performance
        self.trade_count = 0
        self.profitable_trades = 0
        
    def log(self, txt, dt=None, doprint=False):
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print(f'{dt.isoformat()} {txt}')
            
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
            
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED, Price: {order.executed.price:.5f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
            else:
                self.log(f'SELL EXECUTED, Price: {order.executed.price:.5f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
                
        self.order = None
        
    def notify_trade(self, trade):
        if trade.isclosed:
            self.trade_count += 1
            if trade.pnl > 0:
                self.profitable_trades += 1
        
    def next(self):
        if self.order:
            return
            
        if not self.position:
            # Check for sufficient price divergence
            if abs(self.divergence[0]) > self.params.divergence_threshold:
                # If assets show different momentum
                if self.crossover1[0] != self.crossover2[0]:
                    if self.crossover1[0] > 0:  # Asset 1 bullish
                        self.order = self.buy(data=self.datas[0], size=self.position_size)
                        self.order = self.sell(data=self.datas[1], size=self.position_size)
                    else:  # Asset 1 bearish
                        self.order = self.sell(data=self.datas[0], size=self.position_size)
                        self.order = self.buy(data=self.datas[1], size=self.position_size)
        else:
            # Exit when signals converge or divergence reduces
            if (self.crossover1[0] == self.crossover2[0]) or \
               (abs(self.divergence[0]) < self.params.divergence_threshold * 0.5):
                self.close(data=self.datas[0])
                self.close(data=self.datas[1])
                
    def stop(self):
        """Called at the end of the backtest"""
        self.log(f'(Fast: {self.p.fast_period}, Slow: {self.p.slow_period}) Ending Value {self.broker.getvalue():.2f}', doprint=True)
        if self.trade_count > 0:
            win_rate = self.profitable_trades / self.trade_count
            self.log(f'Win Rate: {win_rate:.2%} ({self.profitable_trades}/{self.trade_count})', doprint=True)

class CorrelationZScoreStrategy(bt.Strategy):
    """Korrelation und Z-Score basierte Pairs Trading Strategie"""
    params = (
        ('period', 60),  # Correlation period
        ('zscore_threshold', 2.0),  # Entry threshold
        ('correlation_threshold', 0.7),  # Minimum correlation
        ('printlog', False)  # Print logging
    )
    
    def __init__(self):
        self.order = None
        self.position_size = 1000
        
        # Calculate correlation
        self.correlation = PearsonR(self.data0, self.data1, period=self.p.period)
        
        # Calculate spread and its z-score
        self.spread = self.data1 - self.data0
        self.zscore = ZScore(self.spread, period=self.p.period)
        
        # Track performance
        self.trade_count = 0
        self.profitable_trades = 0
        
    def log(self, txt, dt=None, doprint=False):
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print(f'{dt.isoformat()} {txt}')
            
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
            
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED, Price: {order.executed.price:.5f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
            else:
                self.log(f'SELL EXECUTED, Price: {order.executed.price:.5f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
                
        self.order = None
        
    def notify_trade(self, trade):
        if trade.isclosed:
            self.trade_count += 1
            if trade.pnl > 0:
                self.profitable_trades += 1
        
    def next(self):
        if self.order:
            return
            
        # Only trade if correlation is high enough
        if abs(self.correlation[0]) < self.p.correlation_threshold:
            return
            
        if not self.position:
            if self.zscore > self.p.zscore_threshold:  # Spread is too wide
                self.order = self.sell(data=self.datas[0], size=self.position_size)
                self.order = self.buy(data=self.datas[1], size=self.position_size)
            elif self.zscore < -self.p.zscore_threshold:  # Spread is too narrow
                self.order = self.buy(data=self.datas[0], size=self.position_size)
                self.order = self.sell(data=self.datas[1], size=self.position_size)
        else:
            if abs(self.zscore) < 0.5:  # Spread has normalized
                self.close(data=self.datas[0])
                self.close(data=self.datas[1])
                
    def stop(self):
        """Called at the end of the backtest"""
        self.log(f'(Period: {self.p.period}, Threshold: {self.p.zscore_threshold}) Ending Value {self.broker.getvalue():.2f}', doprint=True)
        if self.trade_count > 0:
            win_rate = self.profitable_trades / self.trade_count
            self.log(f'Win Rate: {win_rate:.2%} ({self.profitable_trades}/{self.trade_count})', doprint=True)

class CovarRatio(bt.Indicator):
    """Berechnet das Verhältnis der Kovarianz zwischen zwei Zeitreihen"""
    lines = ('covar',)
    params = (('period', 20),)
    
    def __init__(self):
        self.addminperiod(self.params.period)
        
    def next(self):
        x = np.array(self.data0.get(size=self.params.period))
        y = np.array(self.data1.get(size=self.params.period))
        covar = np.cov(x, y)[0][1]
        self.lines.covar[0] = covar

class PearsonR(bt.Indicator):
    """Berechnet die Pearson Korrelation zwischen zwei Zeitreihen"""
    lines = ('correlation',)
    params = (('period', 20),)
    
    def __init__(self):
        self.addminperiod(self.params.period)
        
    def next(self):
        x = np.array(self.data0.get(size=self.params.period))
        y = np.array(self.data1.get(size=self.params.period))
        correlation = np.corrcoef(x, y)[0][1]
        self.lines.correlation[0] = correlation

class ZScore(bt.Indicator):
    """Berechnet den Z-Score einer Zeitreihe"""
    lines = ('zscore',)
    params = (('period', 20),)
    
    def __init__(self):
        self.addminperiod(self.params.period)
        
    def next(self):
        data = np.array(self.data0.get(size=self.params.period))
        mean = np.mean(data)
        std = np.std(data)
        if std > 0:
            zscore = (data[-1] - mean) / std
        else:
            zscore = 0
        self.lines.zscore[0] = zscore

class KalmanFilterIndicator(bt.Indicator):
    """Kalman Filter Indicator for tracking the state of a pairs relationship"""
    lines = ('state',)
    params = (
        ('delta', 0.0001),  # Process variance
        ('R', 0.01),        # Measurement variance
    )
    
    def __init__(self):
        super(KalmanFilterIndicator, self).__init__()
        
        # Initial state
        self.state_mean = 0.0
        self.state_var = 1.0
        
    def next(self):
        # Get prices
        price1 = self.data0[0]
        price2 = self.data1[0]
        
        if not (np.isnan(price1) or np.isnan(price2)):
            # Calculate spread
            spread = price2 - price1
            
            # Prediction
            state_pred = self.state_mean
            pred_var = self.state_var + self.p.delta
            
            # Kalman gain
            kalman_gain = pred_var / (pred_var + self.p.R)
            
            # Update
            self.state_mean = state_pred + kalman_gain * (spread - state_pred)
            self.state_var = (1 - kalman_gain) * pred_var
            
            # Store state estimate
            self.lines.state[0] = self.state_mean
        else:
            self.lines.state[0] = float('nan')


class KalmanFilterStrategy(bt.Strategy):
    """Kalman Filter basierte Pairs Trading Strategie"""
    
    params = (
        ('delta', 0.0001),  # Delta für Kalman Filter
        ('R', 0.01),        # Messrauschen
        ('printlog', False)  # Print logging
    )
    
    def __init__(self):
        self.order = None
        self.position_size = 1000
        
        # Initialize indicators
        self.kf = KalmanFilterIndicator(
            self.datas[0],
            self.datas[1],
            delta=self.p.delta,
            R=self.p.R
        )
        
        # Track performance
        self.trade_count = 0
        self.profitable_trades = 0
        
    def log(self, txt, dt=None, doprint=False):
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print(f'{dt.isoformat()} {txt}')
            
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
            
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED, Price: {order.executed.price:.5f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
            else:
                self.log(f'SELL EXECUTED, Price: {order.executed.price:.5f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
                
        self.order = None
        
    def notify_trade(self, trade):
        if trade.isclosed:
            self.trade_count += 1
            if trade.pnl > 0:
                self.profitable_trades += 1
        
    def next(self):
        if self.order:
            return
            
        # Get current state estimate
        state = self.kf[0]
        
        if not self.position:
            if state > 1.0:  # Asset 1 overvalued relative to Asset 2
                self.order = self.sell(data=self.datas[0], size=self.position_size)
                self.order = self.buy(data=self.datas[1], size=self.position_size)
            elif state < -1.0:  # Asset 1 undervalued relative to Asset 2
                self.order = self.buy(data=self.datas[0], size=self.position_size)
                self.order = self.sell(data=self.datas[1], size=self.position_size)
        else:
            if abs(state) < 0.1:  # Close position when spread normalizes
                self.close(data=self.datas[0])
                self.close(data=self.datas[1])
                
    def stop(self):
        """Called at the end of the backtest"""
        self.log(f'(Delta: {self.p.delta:.5f}, R: {self.p.R:.5f}) Ending Value {self.broker.getvalue():.2f}', doprint=True)
        if self.trade_count > 0:
            win_rate = self.profitable_trades / self.trade_count
            self.log(f'Win Rate: {win_rate:.2%} ({self.profitable_trades}/{self.trade_count})', doprint=True)

class BetaResidualStrategy(bt.Strategy):
    """Beta und Residual basierte Pairs Trading Strategie"""
    
    params = (
        ('period', 60),  # Lookback period for beta calculation
        ('printlog', False)  # Print logging
    )
    
    def __init__(self):
        self.order = None
        self.position_size = 1000
        
        # Calculate OLS regression
        self.ols = OLS(self.data0, self.data1, period=self.p.period)
        
        # Calculate residuals
        self.residuals = OLS_Residuals(self.data0, self.data1, period=self.p.period)
        
        # Calculate z-score of residuals
        self.zscore = ZScore(self.residuals.residuals, period=self.p.period)
        
        # Track performance
        self.trade_count = 0
        self.profitable_trades = 0
        
    def log(self, txt, dt=None, doprint=False):
        if self.params.printlog or doprint:
            dt = dt or self.datas[0].datetime.date(0)
            print(f'{dt.isoformat()} {txt}')
            
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            return
            
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(f'BUY EXECUTED, Price: {order.executed.price:.5f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
            else:
                self.log(f'SELL EXECUTED, Price: {order.executed.price:.5f}, Cost: {order.executed.value:.2f}, Comm: {order.executed.comm:.2f}')
                
        self.order = None
        
    def notify_trade(self, trade):
        if trade.isclosed:
            self.trade_count += 1
            if trade.pnl > 0:
                self.profitable_trades += 1
        
    def next(self):
        if self.order:
            return
            
        if not self.position:
            if self.zscore > 2.0:  # Residuals are significantly positive
                self.order = self.sell(data=self.datas[0], size=self.position_size)
                hedge_size = int(self.position_size * self.ols.beta[0])
                self.order = self.buy(data=self.datas[1], size=hedge_size)
            elif self.zscore < -2.0:  # Residuals are significantly negative
                self.order = self.buy(data=self.datas[0], size=self.position_size)
                hedge_size = int(self.position_size * self.ols.beta[0])
                self.order = self.sell(data=self.datas[1], size=hedge_size)
        else:
            if abs(self.zscore) < 0.5:  # Close position when spread normalizes
                self.close(data=self.datas[0])
                self.close(data=self.datas[1])
                
    def stop(self):
        """Called at the end of the backtest"""
        self.log(f'(Period {self.p.period}) Ending Value {self.broker.getvalue():.2f}', doprint=True)
        if self.trade_count > 0:
            win_rate = self.profitable_trades / self.trade_count
            self.log(f'Win Rate: {win_rate:.2%} ({self.profitable_trades}/{self.trade_count})', doprint=True)

class OLS(bt.Indicator):
    """Simple OLS regression indicator"""
    lines = ('beta', 'alpha')
    params = (('period', 20),)
    
    def __init__(self):
        self.addminperiod(self.params.period)
        
    def next(self):
        x = np.array(self.data0.get(size=self.params.period))
        y = np.array(self.data1.get(size=self.params.period))
        
        if len(x) == self.params.period:
            X = np.vstack([x, np.ones(len(x))]).T
            beta, alpha = np.linalg.lstsq(X, y, rcond=None)[0]
            
            self.lines.beta[0] = beta
            self.lines.alpha[0] = alpha
        else:
            self.lines.beta[0] = float('nan')
            self.lines.alpha[0] = float('nan')

class OLS_Residuals(bt.Indicator):
    """Calculate residuals from OLS regression"""
    lines = ('residuals',)
    params = (('period', 20),)
    
    def __init__(self):
        self.addminperiod(self.params.period)
        self.ols = OLS(self.data0, self.data1, period=self.params.period)
        
    def next(self):
        if not np.isnan(self.ols.beta[0]):
            predicted = self.ols.beta[0] * self.data0[0] + self.ols.alpha[0]
            self.lines.residuals[0] = self.data1[0] - predicted
        else:
            self.lines.residuals[0] = float('nan')

class CustomPandasData(bt.feeds.PandasData):
    """Custom data feed"""
    params = {
        'datetime': None,  # Use index as datetime
        'open': 'Open',
        'high': 'High',
        'low': 'Low',
        'close': 'Close',
        'volume': 'Volume',
        'openinterest': None,
    }

def load_and_prepare_data():
    """Load and prepare data with proper error handling"""
    try:
        data_file = os.path.join('data', 'EURUSD.csv')
        print(f"\nLade Daten aus {data_file}...")
        
        if not os.path.exists(data_file):
            raise FileNotFoundError(f"Datendatei nicht gefunden: {data_file}")
            
        # Read data
        data = pd.read_csv(data_file, parse_dates=True, index_col='datetime')
        print(f"Originaldaten: {len(data)} Einträge\n")
        
        # Display sample
        print("Bereinigte Daten:")
        print(data.head())
        
        # Remove rows with zero volume or identical prices
        data = data[data['Volume'] > 0]
        data = data[data['High'] != data['Low']]
        
        print(f"\nFinale Datenpunkte: {len(data)}")
        return data
        
    except Exception as e:
        print(f"Fehler beim Laden der Daten: {str(e)}")
        return None

def create_synthetic_pair(data):
    """Create synthetic pair data with proper error handling"""
    try:
        print("\nErstelle synthetische Daten...")
        
        # Create copy of original data with slight modifications
        synthetic = data.copy()
        
        # Add some noise to create a correlated but different series
        noise = np.random.normal(0, 0.0001, len(data))
        synthetic['Close'] = synthetic['Close'] * (1 + noise)
        synthetic['Open'] = synthetic['Open'] * (1 + noise)
        synthetic['High'] = synthetic['High'] * (1 + noise)
        synthetic['Low'] = synthetic['Low'] * (1 + noise)
        
        return data, synthetic
        
    except Exception as e:
        print(f"Fehler beim Erstellen synthetischer Daten: {str(e)}")
        return None, None

def create_data_feed(df, name=''):
    """Create a Backtrader data feed from a DataFrame"""
    try:
        # Create PandasData feed directly from DataFrame
        data = CustomPandasData(
            dataname=df,
            timeframe=bt.TimeFrame.Minutes,
            compression=60  # 1-hour bars
        )
        
        return data
        
    except Exception as e:
        print(f"Error creating data feed: {str(e)}")
        import traceback
        print(traceback.format_exc())
        return None

def run_strategy(cerebro, strategy_name, strategy_class, strategy_params):
    """Run a single strategy with proper error handling"""
    try:
        print(f"\nStarte Backtest für {strategy_name}...")
        
        # Add strategy with parameters
        cerebro.addstrategy(strategy_class, **strategy_params)
        
        # Run the backtest
        results = cerebro.run()
        
        if not results:
            print(f"Warnung: Keine Ergebnisse für {strategy_name}")
            return None
            
        return results[0]
    except Exception as e:
        print(f"Fehler bei Strategie {strategy_name}: {str(e)}")
        print("Details zum Fehler:")
        import traceback
        traceback.print_exc()
        return None

def prepare_cerebro(data1, data2, initial_cash=100000.0):
    """Prepare a cerebro instance with proper data feeds"""
    try:
        cerebro = bt.Cerebro()
        
        # Ensure data is properly aligned
        if len(data1) != len(data2):
            print("Warnung: Datenlängen stimmen nicht überein. Aligniere Daten...")
            common_index = data1.index.intersection(data2.index)
            data1 = data1.loc[common_index]
            data2 = data2.loc[common_index]
        
        # Create data feeds
        data1_feed = CustomPandasData(dataname=data1)
        data2_feed = CustomPandasData(dataname=data2)
        
        # Add data feeds
        cerebro.adddata(data1_feed)
        cerebro.adddata(data2_feed)
        
        # Set broker parameters
        cerebro.broker.setcash(initial_cash)
        cerebro.broker.setcommission(commission=0.001)  # 0.1% commission
        
        # Add analyzers
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
        cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
        
        return cerebro
    except Exception as e:
        print(f"Fehler bei der Cerebro-Initialisierung: {str(e)}")
        print("Details zum Fehler:")
        import traceback
        traceback.print_exc()
        return None

def main():
    try:
        # Load and prepare data
        data = load_and_prepare_data()
        if data is None:
            print("Fehler beim Laden der Daten. Beende Programm.")
            return
            
        # Create synthetic pair
        data1, data2 = create_synthetic_pair(data)
        if data1 is None or data2 is None:
            print("Fehler beim Erstellen der synthetischen Daten. Beende Programm.")
            return
            
        # Initialize strategies with proper parameters
        strategies = [
            {
                'name': 'Simple MA',
                'class': SimpleMAStrategy,
                'params': {
                    'fast_period': 5,
                    'slow_period': 15,
                    'divergence_threshold': 0.0002,
                    'printlog': True
                }
            },
            {
                'name': 'Correlation + Z-Score',
                'class': CorrelationZScoreStrategy,
                'params': {
                    'period': 60,
                    'zscore_threshold': 2.0,
                    'correlation_threshold': 0.7,
                    'printlog': True
                }
            },
            {
                'name': 'Beta + Residual',
                'class': BetaResidualStrategy,
                'params': {
                    'lookback': 60,
                    'entry_threshold': 2.0,
                    'exit_threshold': 0.5,
                    'printlog': True
                }
            },
            {
                'name': 'Kalman Filter',
                'class': KalmanFilterStrategy,
                'params': {
                    'delta': 0.0001,
                    'R': 0.001,
                    'printlog': True
                }
            }
        ]
        
        # Run each strategy
        for strategy in strategies:
            # Create fresh cerebro instance for each strategy
            cerebro = prepare_cerebro(data1, data2)
            if cerebro is None:
                print(f"Überspringe Strategie {strategy['name']} aufgrund von Initialisierungsfehler")
                continue
                
            # Add strategy
            cerebro.addstrategy(strategy['class'], **strategy['params'])
            
            try:
                print(f"\nStarte Backtest für {strategy['name']}...")
                results = cerebro.run()
                
                if results and len(results) > 0:
                    strat = results[0]
                    
                    # Print performance metrics
                    print(f"\nPerformance Metriken für {strategy['name']}:")
                    sharpe = strat.analyzers.sharpe.get_analysis().get('sharperatio', 0.0)
                    drawdown = strat.analyzers.drawdown.get_analysis().get('max', {}).get('drawdown', 0.0)
                    returns = strat.analyzers.returns.get_analysis().get('rtot', 0.0)
                    
                    print(f"Sharpe Ratio: {sharpe:.2f}")
                    print(f"Max Drawdown: {drawdown:.2%}")
                    print(f"Total Return: {returns:.2%}")
            except Exception as e:
                print(f"Fehler bei Strategie {strategy['name']}: {str(e)}")
                print("Details zum Fehler:")
                import traceback
                traceback.print_exc()
                continue
                
        print("\nBacktest abgeschlossen!")
        
    except Exception as e:
        print(f"Unerwarteter Fehler: {str(e)}")
        print("Details zum Fehler:")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()
