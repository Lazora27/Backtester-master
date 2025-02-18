import backtrader as bt
from itertools import combinations
from typing import Dict, Type, List
from .base_strategy import FlexibleStrategy

class IndicatorPair:
    """Repräsentiert ein Paar von Indikatoren mit ihrer Konfiguration"""
    def __init__(self, name1: str, indicator1: Dict, name2: str, indicator2: Dict):
        self.name1 = name1
        self.indicator1 = indicator1
        self.name2 = name2
        self.indicator2 = indicator2
        
    def get_strategy_params(self) -> dict:
        """Erstellt die Strategie-Parameter für dieses Indikatorpaar"""
        return {
            'indicators': {
                self.name1: self.indicator1,
                self.name2: self.indicator2
            },
            'weights': {
                self.name1: 1.0,
                self.name2: 1.0
            }
        }

class PairStrategy(FlexibleStrategy):
    """Strategie-Klasse für ein spezifisches Indikatorpaar"""
    def __init__(self):
        super().__init__()
        self.pair_name = f"{list(self.p.indicators.keys())[0]}_{list(self.p.indicators.keys())[1]}"

def create_indicator_pairs(chunk_size: int = 100) -> List[Type[PairStrategy]]:
    """
    Erstellt Indikatorpaare als Strategien in Chunks
    
    Args:
        chunk_size: Anzahl der Paare pro Chunk
    
    Returns:
        Generator der Strategie-Klassen in Chunks
    """
    
    # Lade alle verfügbaren Indikatoren dynamisch
    import os
    import importlib
    import inspect
    
    indicators_path = os.path.join(os.path.dirname(__file__), '..', 'Indikatoren')
    
    AVAILABLE_INDICATORS = {}
    
    # Durchsuche rekursiv nach Indikatoren
    for root, _, files in os.walk(indicators_path):
        for file in files:
            if file.endswith('.py') and not file.startswith('__'):
                # Konvertiere Dateipfad zu Modulpfad
                rel_path = os.path.relpath(root, os.path.dirname(indicators_path))
                module_path = os.path.join(rel_path, file[:-3]).replace(os.path.sep, '.')
                
                try:
                    module = importlib.import_module(module_path)
                    # Finde alle Klassen im Modul die von bt.Indicator erben
                    for name, obj in inspect.getmembers(module):
                        if (inspect.isclass(obj) and 
                            issubclass(obj, bt.Indicator) and 
                            obj != bt.Indicator):
                            
                            AVAILABLE_INDICATORS[f"{module_path}.{name}"] = {
                                'class': obj,
                                'params': getattr(obj, 'params', {})
                            }
                except Exception as e:
                    print(f"Konnte Modul {module_path} nicht laden: {e}")
    
    # Erstelle alle möglichen Paare
    all_pairs = list(combinations(AVAILABLE_INDICATORS.items(), 2))
    total_pairs = len(all_pairs)
    
    print(f"Gefundene Indikatoren: {len(AVAILABLE_INDICATORS)}")
    print(f"Mögliche Paare: {total_pairs}")
    
    # Verarbeite Paare in Chunks
    for i in range(0, total_pairs, chunk_size):
        chunk_pairs = []
        for (name1, ind1), (name2, ind2) in all_pairs[i:i + chunk_size]:
            # Erstelle ein neues Paar
            pair = IndicatorPair(name1, ind1, name2, ind2)
            
            # Erstelle eine neue Strategie-Klasse für dieses Paar
            strategy_name = f"Pair_{i}_{name1.split('.')[-1]}_{name2.split('.')[-1]}"
            strategy_class = type(strategy_name, (PairStrategy,), {
                'params': pair.get_strategy_params()
            })
            
            chunk_pairs.append(strategy_class)
            
        yield chunk_pairs

def run_pair_analysis(data_feed, chunk_size: int = 100):
    """
    Führt die Analyse für alle Indikatorpaare durch
    
    Args:
        data_feed: Backtrader-Datenfeed
        chunk_size: Anzahl der Paare die gleichzeitig analysiert werden
    """
    results = []
    
    for chunk in create_indicator_pairs(chunk_size):
        chunk_results = []
        for Strategy in chunk:
            cerebro = bt.Cerebro()
            cerebro.adddata(data_feed)
            cerebro.addstrategy(Strategy)
            cerebro.broker.setcash(100000.0)
            
            initial = cerebro.broker.getvalue()
            result = cerebro.run()
            final = cerebro.broker.getvalue()
            
            strategy = result[0]
            chunk_results.append({
                'pair': strategy.pair_name,
                'return': (final - initial) / initial * 100,
                'trades': len(strategy.trades)
            })
        
        # Sortiere Chunk-Ergebnisse nach Rendite
        chunk_results.sort(key=lambda x: x['return'], reverse=True)
        
        # Behalte nur die besten 10% aus jedem Chunk
        top_n = max(1, len(chunk_results) // 10)
        results.extend(chunk_results[:top_n])
    
    # Sortiere Gesamtergebnisse nach Rendite
    results.sort(key=lambda x: x['return'], reverse=True)
    return results
