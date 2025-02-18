import backtrader as bt
import itertools
import os
import sys
import importlib.util
import json
import pandas as pd
from concurrent.futures import ProcessPoolExecutor
from typing import List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path

# Füge das Hauptverzeichnis zum Python-Pfad hinzu
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(root_dir)
sys.path.append(os.path.join(root_dir, "Indikatoren"))

from strategies.base_strategy import FlexibleStrategy

class UniversalIndicatorTester:
    """
    Universeller Indikator-Tester der alle möglichen Kombinationen von Indikatoren testet
    und die Ergebnisse speichert.
    """
    
    def __init__(self, data_path: str, indicators_dir: str, results_dir: str = "test_results"):
        self.data_path = data_path
        self.indicators_dir = Path(indicators_dir)
        self.results_dir = Path(results_dir)
        self.results_dir.mkdir(exist_ok=True)
        
        # Lade alle verfügbaren Indikatoren
        self.indicators = self._load_indicators()
        
    def _load_indicators(self) -> Dict[str, Any]:
        """Lädt alle Indikatoren aus dem indicators_dir"""
        indicators = {}
        print(f"\nSuche Indikatoren in: {self.indicators_dir}")
        
        # Rekursiv durch alle Python-Dateien im indicators_dir gehen
        for file_path in Path(self.indicators_dir).rglob("*.py"):
            if file_path.name.startswith("__") or "__pycache__" in str(file_path):
                continue
                
            print(f"\nVersuche Indikator zu laden: {file_path}")
            try:
                # Versuche das Modul direkt zu importieren
                spec = importlib.util.spec_from_file_location(
                    file_path.stem, str(file_path)
                )
                if spec is None or spec.loader is None:
                    print(f"Konnte spec nicht erstellen für: {file_path}")
                    continue
                    
                module = importlib.util.module_from_spec(spec)
                sys.modules[file_path.stem] = module
                spec.loader.exec_module(module)
                
                # Suche nach Indikator-Klassen im Modul
                for name, obj in module.__dict__.items():
                    if (isinstance(obj, type) and 
                        hasattr(obj, "lines") and  # Backtrader Indikatoren haben 'lines'
                        not name.startswith("_")):
                        
                        # Erstelle einen aussagekräftigen Namen für den Indikator
                        category = file_path.parent.name
                        indicator_name = f"{category}.{name}"
                        indicators[indicator_name] = obj
                        print(f"✓ Indikator geladen: {indicator_name}")
                        
            except Exception as e:
                print(f"✗ Fehler beim Laden von {file_path}: {str(e)}")
                import traceback
                print(traceback.format_exc())
                
        print(f"\nErfolgreich {len(indicators)} Indikatoren geladen.")
        return indicators
        
    def _create_strategy(self, indicator_combination: List[str]) -> type:
        """Erstellt eine neue Strategie-Klasse mit der gegebenen Indikator-Kombination"""
        
        class DynamicStrategy(FlexibleStrategy):
            params = (
                ("indicators", {
                    ind_name: {
                        "class": self.indicators[ind_name],
                        "params": {}  # Default Parameter
                    }
                    for ind_name in indicator_combination
                }),
                ("weights", {
                    ind_name: 1.0  # Gleiche Gewichtung
                    for ind_name in indicator_combination
                })
            )
            
        return DynamicStrategy
        
    def _run_backtest(self, strategy_class: type) -> Dict[str, float]:
        """Führt einen einzelnen Backtest durch"""
        cerebro = bt.Cerebro()
        
        # Daten laden
        data = bt.feeds.GenericCSVData(
            dataname=self.data_path,
            dtformat="%d.%m.%Y %H:%M:%S",
            datetime=0,
            open=1,
            high=2,
            low=3,
            close=4,
            volume=5,
            openinterest=-1,
            headers=True  # CSV hat Header
        )
        
        cerebro.adddata(data)
        cerebro.addstrategy(strategy_class)
        
        # Analyzers hinzufügen
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name="sharpe")
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name="drawdown")
        cerebro.addanalyzer(bt.analyzers.Returns, _name="returns")
        cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="trades")
        
        # Backtest durchführen
        results = cerebro.run()
        
        # Metriken extrahieren
        strat = results[0]
        return {
            "sharpe_ratio": strat.analyzers.sharpe.get_analysis()["sharperatio"],
            "max_drawdown": strat.analyzers.drawdown.get_analysis()["max"]["drawdown"],
            "total_return": strat.analyzers.returns.get_analysis()["rtot"],
            "trade_count": strat.analyzers.trades.get_analysis().get("total", {}).get("total", 0)
        }
        
    def test_combinations(self, max_indicators: int = 3, parallel: bool = True) -> pd.DataFrame:
        """
        Testet alle möglichen Indikator-Kombinationen
        
        Args:
            max_indicators: Maximale Anzahl von Indikatoren pro Kombination
            parallel: Ob die Tests parallel ausgeführt werden sollen
        
        Returns:
            DataFrame mit den Testergebnissen
        """
        results = []
        
        # Generiere alle möglichen Kombinationen
        for n in range(1, max_indicators + 1):
            combinations = list(itertools.combinations(self.indicators.keys(), n))
            print(f"Teste {len(combinations)} Kombinationen mit {n} Indikatoren...")
            
            if parallel and len(combinations) > 1:
                with ProcessPoolExecutor() as executor:
                    for combo in combinations:
                        try:
                            strategy = self._create_strategy(combo)
                            future = executor.submit(self._run_backtest, strategy)
                            metrics = future.result()
                            
                            results.append({
                                "indicators": list(combo),
                                "num_indicators": len(combo),
                                **metrics
                            })
                        except Exception as e:
                            print(f"Fehler bei Kombination {combo}: {e}")
            else:
                for combo in combinations:
                    try:
                        strategy = self._create_strategy(combo)
                        metrics = self._run_backtest(strategy)
                        
                        results.append({
                            "indicators": list(combo),
                            "num_indicators": len(combo),
                            **metrics
                        })
                    except Exception as e:
                        print(f"Fehler bei Kombination {combo}: {e}")
                    
        if not results:
            print("Keine Ergebnisse gefunden!")
            return pd.DataFrame()
            
        # Erstelle DataFrame
        df = pd.DataFrame(results)
        
        # Speichere Ergebnisse
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        results_file = self.results_dir / f"results_{timestamp}.csv"
        df.to_csv(results_file, index=False)
        print(f"\nErgebnisse gespeichert in: {results_file}")
        
        # Zeige Top 10 Strategien
        if len(df) > 0:
            print("\nTop 10 Strategien nach Sharpe Ratio:")
            top_10 = df.nlargest(10, "sharpe_ratio")[["indicators", "sharpe_ratio", "total_return", "max_drawdown"]]
            print(top_10.to_string())
        
        return df

if __name__ == "__main__":
    # Beispiel-Verwendung
    tester = UniversalIndicatorTester(
        data_path="./Example_HisData/data/EURUSD.csv",  # Korrekter Datenpfad
        indicators_dir="./Indikatoren"  # Korrekter Indikatoren-Pfad
    )
    
    print(f"\nGefundene Indikatoren: {len(tester.indicators)}")
    if tester.indicators:
        print("\nVerfügbare Indikatoren:")
        for name in sorted(tester.indicators.keys()):
            print(f"- {name}")
    
    # Teste alle Kombinationen mit max. 3 Indikatoren
    results = tester.test_combinations(max_indicators=3, parallel=True)
