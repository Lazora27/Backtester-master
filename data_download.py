import yfinance as yf
import os
from datetime import datetime

def download_forex_data():
    # Erstelle Verzeichnis falls es nicht existiert
    data_dir = "Yahoo_HistoricalData"
    os.makedirs(data_dir, exist_ok=True)
    
    # Download EURUSD Daten
    symbol = "EURUSD=X"
    start_date = "2023-01-01"
    end_date = "2024-01-01"
    
    print(f"Lade {symbol} Daten von {start_date} bis {end_date}...")
    
    # Lade Daten
    data = yf.download(
        symbol,
        start=start_date,
        end=end_date,
        interval="1h"
    )
    
    # Speichere Daten
    filename = os.path.join(data_dir, f"EURUSD_1H_{start_date}_{end_date}.csv")
    data.to_csv(filename)
    
    print(f"Daten gespeichert in: {filename}")
    print(f"Anzahl der Datenpunkte: {len(data)}")
    
if __name__ == "__main__":
    download_forex_data()
