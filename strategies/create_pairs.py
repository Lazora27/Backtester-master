import os
import sys
import importlib
import inspect
import backtrader as bt
from typing import List, Dict
import json
from pathlib import Path

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def find_all_indicators() -> Dict[str, type]:
    """Findet alle Indikatoren im Projekt"""
    indicators = {}
    indicators_path = os.path.join(os.path.dirname(__file__), '..', 'Indikatoren')
    
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
                            
                            indicators[f"{name}"] = obj
                except Exception as e:
                    print(f"Konnte Modul {module_path} nicht laden: {e}")
    
    return indicators

def create_strategy_file(ind1_name: str, ind1_class: type, 
                        ind2_name: str, ind2_class: type, 
                        output_dir: str):
    """Erstellt eine Strategiedatei für ein Indikatorpaar"""
    
    strategy_name = f"{ind1_name}_{ind2_name}_Strategy"
    file_name = f"{strategy_name.lower()}.py"
    file_path = os.path.join(output_dir, file_name)
    
    # Erstelle den Strategiecode
    code = f"""import backtrader as bt
from ..base_strategy import FlexibleStrategy

class {strategy_name}(FlexibleStrategy):
    \"\"\"
    Kombinierte Strategie von {ind1_name} und {ind2_name}
    \"\"\"
    
    params = (
        ('indicators', {{
            '{ind1_name}': {{
                'class': {ind1_name},
                'params': {getattr(ind1_class, 'params', {})}
            }},
            '{ind2_name}': {{
                'class': {ind2_name},
                'params': {getattr(ind2_class, 'params', {})}
            }}
        }}),
        ('weights', {{
            '{ind1_name}': 1.0,
            '{ind2_name}': 1.0
        }})
    )
"""
    
    # Schreibe die Datei
    with open(file_path, 'w') as f:
        f.write(code)
    
    return file_path

def main():
    # Erstelle Verzeichnis für die Indikatorpaare
    base_dir = os.path.dirname(os.path.dirname(__file__))
    pairs_dir = os.path.join(base_dir, 'Indikator-Pairing_x2')
    os.makedirs(pairs_dir, exist_ok=True)
    
    # Finde alle Indikatoren
    indicators = find_all_indicators()
    
    # Erstelle eine Liste für das Tracking der Paare
    pairs_list = []
    
    # Systematisches Pairing
    indicator_items = list(indicators.items())
    total_indicators = len(indicator_items)
    total_pairs = (total_indicators * (total_indicators - 1)) // 2
    
    print(f"Gefundene Indikatoren: {total_indicators}")
    print(f"Mögliche Paare: {total_pairs}")
    print("\nStarte Pairing-Prozess...")
    
    # Fortschrittsanzeige initialisieren
    pairs_created = 0
    
    # Erstelle Kategorien-Ordner
    for i, (ind1_name, ind1_class) in enumerate(indicator_items):
        remaining_pairs = ((total_indicators - i) * (total_indicators - i - 1)) // 2
        print(f"\nPaare für {ind1_name} ({i+1}/{total_indicators}):")
        print(f"Noch zu erstellende Paare: {remaining_pairs}")
        
        # Erstelle Unterordner für jeden Basis-Indikator
        ind_dir = os.path.join(pairs_dir, f"{ind1_name}_pairs")
        os.makedirs(ind_dir, exist_ok=True)
        
        # Paare mit allen nachfolgenden Indikatoren
        for j in range(i + 1, total_indicators):
            ind2_name, ind2_class = indicator_items[j]
            
            pairs_created += 1
            progress = (pairs_created / total_pairs) * 100
            
            print(f"  - Erstelle Paar mit {ind2_name} ({progress:.1f}% abgeschlossen)")
            
            # Erstelle Strategiedatei
            strategy_file = create_strategy_file(
                ind1_name, ind1_class,
                ind2_name, ind2_class,
                ind_dir
            )
            
            # Tracking der erstellten Paare
            pairs_list.append({
                'indicator1': ind1_name,
                'indicator2': ind2_name,
                'strategy_file': os.path.relpath(strategy_file, pairs_dir)
            })
            
            # Speichere die Liste periodisch
            if pairs_created % 100 == 0:
                pairs_json = os.path.join(pairs_dir, 'pairs_list.json')
                with open(pairs_json, 'w') as f:
                    json.dump(pairs_list, f, indent=2)
    
    # Finale Speicherung der Liste aller Paare
    pairs_json = os.path.join(pairs_dir, 'pairs_list.json')
    with open(pairs_json, 'w') as f:
        json.dump(pairs_list, f, indent=2)
    
    print(f"\nFertig! Erstellt {len(pairs_list)} Strategiedateien in {pairs_dir}")
    print(f"Liste aller Paare wurde gespeichert in: {pairs_json}")

if __name__ == "__main__":
    main()
