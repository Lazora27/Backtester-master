import backtrader as bt
import pandas as pd
import numpy as np
import logging
from typing import Optional, Dict, List
from indicator_handler import IndicatorHandler
import os
from datetime import datetime

# Logging-Konfiguration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FlexibleStrategy(bt.Strategy):
    params = (
        ('indicator_names', []),
        ('indicator_params', {}),
        ('indicator_handler', None),
    )

    def __init__(self):
        """
        Initialisiere die Strategie
        """
        self.order = None
        self.trades = []
        self.position_size = 2.0
        
        # Erstelle Indikatoren
        self.indicators = {}
        for name in self.params.indicator_names:
            try:
                indicator = self.p.indicator_handler.create_indicator(name, **self.p.indicator_params.get(name, {}))
                if indicator:
                    self.indicators[name] = indicator
                    logger.info(f"Indikator {name} erfolgreich erstellt")
                else:
                    logger.error(f"Fehler beim Erstellen von {name}")
            except Exception as e:
                logger.error(f"Fehler beim Erstellen von {name}: {str(e)}")

    def get_combined_signal(self) -> float:
        """
        Kombiniere die Signale aller Indikatoren
        
        Returns:
            float: Kombiniertes Signal zwischen -1 und 1
        """
        try:
            signals = []
            for name, indicator in self.indicators.items():
                if indicator is not None and len(indicator) > 0:
                    signal = self.p.indicator_handler.get_signal(name, indicator)
                    if signal is not None:
                        signals.append(signal)
            
            # Wenn keine gültigen Signale, kein Handel
            if not signals:
                return 0
                
            # Berechne Durchschnitt der Signale
            return sum(signals) / len(signals)
            
        except Exception as e:
            logger.error(f"Fehler bei Signal-Berechnung: {str(e)}")
            return 0

    def next(self):
        """
        Haupthandelsfunktion - wird für jeden Zeitschritt aufgerufen
        """
        # Wenn eine Order aktiv ist, nichts tun
        if self.order:
            return
            
        # Berechne kombiniertes Signal
        signal = self.get_combined_signal()
        
        # Wenn wir eine Position haben
        if self.position:
            # Long Position
            if self.position.size > 0:
                if signal < -0.3:  # Schließe Long wenn Signal unter -0.3
                    logger.info(f"{self.data.datetime.date(0)} CLOSE POSITION, Signal: {signal:.2f}")
                    self.order = self.close()
            # Short Position
            else:
                if signal > 0.3:  # Schließe Short wenn Signal über 0.3
                    logger.info(f"{self.data.datetime.date(0)} CLOSE POSITION, Signal: {signal:.2f}")
                    self.order = self.close()
        
        # Wenn wir keine Position haben
        else:
            if signal > 0.7:  # Öffne Long wenn Signal über 0.7
                logger.info(f"{self.data.datetime.date(0)} BUY CREATE, Signal: {signal:.2f}, Size: {self.position_size:.2f}")
                self.order = self.buy(size=self.position_size)
            elif signal < -0.7:  # Öffne Short wenn Signal unter -0.7
                logger.info(f"{self.data.datetime.date(0)} SELL CREATE, Signal: {signal:.2f}, Size: {self.position_size:.2f}")
                self.order = self.sell(size=self.position_size)

    def notify_order(self, order):
        """
        Wird bei Order-Updates aufgerufen
        
        Args:
            order: Order-Objekt
        """
        if order.status in [order.Submitted, order.Accepted]:
            return

        if order.status in [order.Completed]:
            if order.isbuy():
                logger.info(f"{self.data.datetime.date(0)} BUY EXECUTED, "
                          f"Price: {order.executed.price:.5f}, "
                          f"Cost: {order.executed.value:.2f}, "
                          f"Comm: {order.executed.comm:.2f}")
            else:
                logger.info(f"{self.data.datetime.date(0)} SELL EXECUTED, "
                          f"Price: {order.executed.price:.5f}, "
                          f"Cost: {order.executed.value:.2f}, "
                          f"Comm: {order.executed.comm:.2f}")

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            logger.info(f"{self.data.datetime.date(0)} Order Canceled/Margin/Rejected")

        self.order = None

    def notify_trade(self, trade):
        """
        Wird bei Trade-Updates aufgerufen
        
        Args:
            trade: Trade-Objekt
        """
        if trade.isclosed:
            self.trades.append(trade)
            logger.info(f"{self.data.datetime.date(0)} OPERATION PROFIT, "
                      f"GROSS: {trade.pnl:.2f}, NET: {trade.pnlcomm:.2f}")

    def get_metrics(self):
        """
        Berechne wichtige Performance-Metriken
        
        Returns:
            dict: Performance-Metriken
        """
        try:
            # Portfolio-Werte
            start_value = self.broker.startingcash
            end_value = self.broker.getvalue()
            
            # Berechne Returns
            total_return = (end_value - start_value) / start_value
            
            # Berechne Win Rate und durchschnittlichen Gewinn
            profitable_trades = len([t for t in self.trades if t.pnlcomm > 0])
            total_trades = len(self.trades)
            win_rate = profitable_trades / total_trades if total_trades > 0 else 0
            avg_profit = sum(t.pnlcomm for t in self.trades) / total_trades if total_trades > 0 else 0
            
            return {
                'total_return': float(total_return),
                'win_rate': float(win_rate),
                'total_trades': total_trades,
                'avg_profit': float(avg_profit),
                'final_value': float(end_value)
            }
            
        except Exception as e:
            logger.error(f"Fehler bei Metrik-Berechnung: {str(e)}")
            return {}


def preprocess_data(data_path: str) -> Optional[str]:
    """
    Bereinige und speichere die Daten
    
    Args:
        data_path: Pfad zur Datendatei
        
    Returns:
        str: Pfad zur bereinigten Datei
    """
    try:
        # Lese Daten
        df = pd.read_csv(data_path)
        
        # Bereinige Daten
        df = df.dropna()
        
        # Speichere bereinigte Daten
        cleaned_path = data_path.replace('.csv', '_cleaned.csv')
        df.to_csv(cleaned_path, index=False)
        
        logger.info(f"Bereinigte Daten gespeichert in: {cleaned_path}")
        return cleaned_path
        
    except Exception as e:
        logger.error(f"Fehler bei Datenbereinigung: {str(e)}")
        return None


def run_backtest(
    data_path: str,
    indicator_names: List[str],
    initial_cash: float = 100000.0,
    commission: float = 0.001,
    indicator_params: Optional[Dict] = None
) -> Optional[Dict]:
    """
    Führe Backtest durch
    
    Args:
        data_path: Pfad zur Datendatei
        indicator_names: Liste der Indikatornamen
        initial_cash: Startkapital
        commission: Kommission pro Trade
        indicator_params: Parameter für Indikatoren
        
    Returns:
        dict: Backtest-Ergebnisse
    """
    try:
        # Bereinige Daten
        cleaned_path = preprocess_data(data_path)
        if not cleaned_path:
            return None
            
        # Initialisiere Backtrader
        cerebro = bt.Cerebro()
        
        # Lade Daten
        data = bt.feeds.GenericCSVData(
            dataname=cleaned_path,
            datetime=0,
            open=1,
            high=2,
            low=3,
            close=4,
            volume=5,
            dtformat='%Y-%m-%d',
            timeframe=bt.TimeFrame.Days
        )
        cerebro.adddata(data)
        
        # Setze Parameter
        cerebro.broker.setcash(initial_cash)
        cerebro.broker.setcommission(commission=commission)
        
        # Erstelle Strategie
        indicator_handler = IndicatorHandler()
        cerebro.addstrategy(
            FlexibleStrategy,
            indicator_names=indicator_names,
            indicator_handler=indicator_handler,
            indicator_params=indicator_params or {}
        )
        
        # Führe Backtest durch
        logger.info(f"Starte Backtest mit Indikatoren: {indicator_names}")
        results = cerebro.run()
        
        if not results:
            logger.error("Keine Ergebnisse vom Backtest")
            return None
            
        strat = results[0]
        
        # Extrahiere Metriken
        metrics = strat.get_metrics()
        
        logger.info("Backtest abgeschlossen:")
        logger.info(f"Indikatoren: {indicator_names}")
        logger.info(f"Total Return: {metrics['total_return']:.2%}")
        logger.info(f"Win Rate: {metrics['win_rate']:.2%}")
        logger.info(f"Trades: {metrics['total_trades']}")
        logger.info(f"Avg Trade: {metrics['avg_profit']:.5f}")
        logger.info(f"Final Value: {metrics['final_value']:.2f}")
        
        return metrics
        
    except Exception as e:
        logger.error(f"Fehler beim Testen: {str(e)}")
        return None


def run_multiple_tests(
    data_path: str,
    indicator_combinations: List[List[str]],
    initial_cash: float = 100000.0,
    commission: float = 0.001,
    indicator_params: Optional[Dict] = None
) -> None:
    """
    Führe mehrere Backtests durch
    
    Args:
        data_path: Pfad zur Datendatei
        indicator_combinations: Liste von Indikator-Kombinationen
        initial_cash: Startkapital
        commission: Kommission pro Trade
        indicator_params: Parameter für Indikatoren
    """
    all_results = []
    
    for indicators in indicator_combinations:
        result = run_backtest(
            data_path=data_path,
            indicator_names=indicators,
            initial_cash=initial_cash,
            commission=commission,
            indicator_params=indicator_params
        )
        
        if result:
            result['indicators'] = indicators
            all_results.append(result)
    
    if all_results:
        # Erstelle Ergebnisverzeichnis
        os.makedirs('test_results', exist_ok=True)
        
        # Erstelle Dateinamen mit Zeitstempel
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        results_file = f'test_results/combined_results_{timestamp}.csv'
        
        # Erstelle DataFrame
        df = pd.DataFrame(all_results)
        
        # Sortiere nach Total Return
        df = df.sort_values('total_return', ascending=False)
        
        # Speichere Ergebnisse
        df.to_csv(results_file, index=False)
        
        print("\nTop Strategien nach Total Return:")
        print(df[['total_return', 'win_rate', 'total_trades', 'avg_profit', 'final_value']].to_string())
        print(f"\nAlle Ergebnisse wurden gespeichert in: {results_file}")
    else:
        print("\nKeine erfolgreichen Tests durchgeführt")
