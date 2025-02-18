import backtrader as bt
from typing import List, Dict, Type
import os
import importlib
import inspect

class IndicatorLoader:
    """
    Klasse zum Laden und Testen von Indikatoren
    """
    def __init__(self, indicators_dir: str = r'C:\Users\nikol\Desktop\backtrader-master\Indikatoren'):
        self.indicators_dir = indicators_dir
        self.indicators = {}

    def load_indicators(self) -> Dict[str, Type[bt.Indicator]]:
        """
        Lädt alle Indikatoren aus dem angegebenen Verzeichnis
        """
        if not os.path.exists(self.indicators_dir):
            raise FileNotFoundError(f'Indikatoren-Verzeichnis {self.indicators_dir} nicht gefunden')

        for root, dirs, files in os.walk(self.indicators_dir):
            for file in files:
                if file.endswith('.py') and not file.startswith('__'):
                    module_name = file[:-3]
                    module_path = os.path.join(root, file)
                    spec = importlib.util.spec_from_file_location(module_name, module_path)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)

                    for name, obj in inspect.getmembers(module):
                        if inspect.isclass(obj) and issubclass(obj, bt.Indicator) and obj != bt.Indicator:
                            self.indicators[name] = obj

        return self.indicators

    def test_indicators(self, data: bt.feeds) -> Dict[str, bool]:
        """
        Testet alle geladenen Indikatoren
        """
        results = {}
        for name, indicator in self.indicators.items():
            try:
                cerebro = bt.Cerebro()
                cerebro.adddata(data)
                cerebro.addstrategy(indicator)
                cerebro.run()
                results[name] = True
            except Exception as e:
                results[name] = False

        return results
