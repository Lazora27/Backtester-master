import backtrader as bt
import itertools
from datetime import datetime
import pandas as pd
from typing import List, Dict, Any
import os
from pathlib import Path
import numpy as np

class CombinedIndicatorStrategy(bt.Strategy):
    """
    Strategie die mehrere Indikatoren kombiniert und deren Signale auswertet
    """
    
    params = (
        ('indicators', []),  # Liste von (Indikator-Klasse, Parameter) Tupeln
    )
    
    def __init__(self):
        self.indicators = []
        self.order = None
        
        # Initialisiere alle Indikatoren
        for ind_class, ind_params in self.p.indicators:
            ind = ind_class(self.data0, **ind_params)
            self.indicators.append(ind)
            
        # Warte mindestens 30 Perioden für genügend Daten
        self.min_period = 30
    
    def next(self):
        # Warte bis genügend Daten verfügbar sind
        if len(self.data) < self.min_period:
            return
            
        if self.order:
            return
            
        # Sammle Signale von allen Indikatoren
        signals = []
        
        for ind in self.indicators:
            try:
                if isinstance(ind, bt.ind.RSI):
                    if ind[0] > 0:  # Prüfe ob Wert gültig ist
                        if ind[0] < 30:  # Überverkauft
                            signals.append(1)
                        elif ind[0] > 70:  # Überkauft
                            signals.append(-1)
                        else:
                            signals.append(0)
                        
                elif isinstance(ind, bt.ind.MACD):
                    if ind.macd[0] is not None and ind.signal[0] is not None:
                        if ind.macd[0] > ind.signal[0]:
                            signals.append(1)
                        elif ind.macd[0] < ind.signal[0]:
                            signals.append(-1)
                        else:
                            signals.append(0)
                        
                elif isinstance(ind, bt.ind.Stochastic):
                    if ind.percK[0] is not None and ind.percD[0] is not None:
                        if ind.percK[0] < 20 and ind.percD[0] < 20:
                            signals.append(1)
                        elif ind.percK[0] > 80 and ind.percD[0] > 80:
                            signals.append(-1)
                        else:
                            signals.append(0)
                        
                elif isinstance(ind, bt.ind.BollingerBands):
                    if ind.lines.mid[0] is not None:
                        if self.data0.close[0] < ind.lines.bot[0]:
                            signals.append(1)
                        elif self.data0.close[0] > ind.lines.top[0]:
                            signals.append(-1)
                        else:
                            signals.append(0)
                            
            except Exception as e:
                continue
        
        # Entscheidungsfindung basierend auf Signalen
        if len(signals) > 0:
            avg_signal = sum(signals) / len(signals)
            
            if avg_signal > 0.5 and not self.position:
                self.order = self.buy()
            elif avg_signal < -0.5 and not self.position:
                self.order = self.sell()
            elif abs(avg_signal) < 0.2 and self.position:
                self.order = self.close()

def test_indicator_combinations(data_path: str, max_indicators: int = 3) -> pd.DataFrame:
    """
    Testet verschiedene Kombinationen von Indikatoren
    
    Args:
        data_path: Pfad zur CSV-Datei mit den Marktdaten
        max_indicators: Maximale Anzahl von Indikatoren pro Kombination
    """
    # Verfügbare Indikatoren und ihre Parameter
    INDICATORS = [
        (bt.ind.RSI, {'period': 14}),
        (bt.ind.MACD, {'period_me1': 12, 'period_me2': 26, 'period_signal': 9}),
        (bt.ind.Stochastic, {'period': 14, 'period_dfast': 3, 'period_dslow': 3}),
        (bt.ind.BollingerBands, {'period': 20, 'devfactor': 2})
    ]
    
    results = []
    
    # Generiere alle möglichen Kombinationen
    for n in range(1, max_indicators + 1):
        for combo in itertools.combinations(INDICATORS, n):
            print(f"\nTeste Kombination: {[ind[0].__name__ for ind in combo]}")
            
            try:
                # Initialisiere Cerebro
                cerebro = bt.Cerebro()
                
                # Setze Startkapital
                cerebro.broker.setcash(100000.0)
                
                # Lade Daten
                data = bt.feeds.GenericCSVData(
                    dataname=data_path,
                    dtformat='%d.%m.%Y %H:%M:%S.000',
                    datetime=0,
                    open=1,
                    high=2,
                    low=3,
                    close=4,
                    volume=5,
                    openinterest=-1,
                    headers=True
                )
                cerebro.adddata(data)
                
                # Füge Strategie hinzu
                cerebro.addstrategy(CombinedIndicatorStrategy, indicators=combo)
                
                # Füge Analysen hinzu
                cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='sharpe')
                cerebro.addanalyzer(bt.analyzers.DrawDown, _name='drawdown')
                cerebro.addanalyzer(bt.analyzers.Returns, _name='returns')
                cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name='trades')
                
                # Führe Backtest durch
                print("Starte Backtest...")
                result = cerebro.run()[0]
                print("Backtest abgeschlossen.")
                
                # Sammle Metriken
                sharpe = result.analyzers.sharpe.get_analysis()
                drawdown = result.analyzers.drawdown.get_analysis()
                returns = result.analyzers.returns.get_analysis()
                trades = result.analyzers.trades.get_analysis()
                
                metrics = {
                    'indicators': [ind[0].__name__ for ind in combo],
                    'num_indicators': len(combo),
                    'sharpe_ratio': sharpe.get('sharperatio', 0.0) or 0.0,
                    'max_drawdown': drawdown.get('max', {}).get('drawdown', 0.0) or 0.0,
                    'total_return': returns.get('rtot', 0.0) or 0.0,
                    'trade_count': trades.get('total', {}).get('total', 0)
                }
                
                results.append(metrics)
                print(f"Sharpe Ratio: {metrics['sharpe_ratio']:.2f}")
                print(f"Max Drawdown: {metrics['max_drawdown']:.2%}")
                print(f"Total Return: {metrics['total_return']:.2%}")
                print(f"Trades: {metrics['trade_count']}")
                
            except Exception as e:
                print(f"Fehler bei Kombination {[ind[0].__name__ for ind in combo]}: {e}")
                continue
    
    if not results:
        print("Keine erfolgreichen Tests!")
        return pd.DataFrame()
    
    # Erstelle DataFrame
    df = pd.DataFrame(results)
    
    # Speichere Ergebnisse
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    results_file = f'test_results/indicator_results_{timestamp}.csv'
    df.to_csv(results_file, index=False)
    print(f"\nErgebnisse gespeichert in: {results_file}")
    
    return df

if __name__ == "__main__":
    # Erstelle Verzeichnisse falls sie nicht existieren
    Path("./test_results").mkdir(exist_ok=True)
    
    # Teste Indikator-Kombinationen
    results = test_indicator_combinations(
        data_path="./Example_HisData/data/EURUSD.csv",
        max_indicators=3
    )
    
    if not results.empty:
        # Zeige Top 10 Strategien
        print("\nTop 10 Strategien nach Sharpe Ratio:")
        top_10 = results.nlargest(10, 'sharpe_ratio')
        print(top_10[['indicators', 'sharpe_ratio', 'total_return', 'max_drawdown']].to_string())
