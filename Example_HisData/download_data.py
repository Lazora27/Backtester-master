import pandas as pd
import requests
from datetime import datetime, timedelta
import time
import os
import struct
from concurrent.futures import ThreadPoolExecutor, as_completed
from calendar import monthrange

def download_tick(pair, year, month, day, hour=0):
    """Download tick data from Dukascopy and save it as CSV"""
    url_prefix = "https://www.dukascopy.com/datafeed"
    
    # Zeitstempel berechnen
    date = datetime(year, month, day, hour)
    timestamp = int(time.mktime(date.timetuple()) * 1000)
    
    # URL erstellen
    url = f"{url_prefix}/{pair}/{year:04d}/{month-1:02d}/{day:02d}/{hour:02d}h_ticks.bi5"
    
    try:
        response = requests.get(url)
        if response.status_code != 200:
            return None
            
        # Daten dekodieren
        data = []
        for i in range(0, len(response.content), 20):
            chunk = response.content[i:i+20]
            if len(chunk) < 20:
                break
                
            timestamp, askp, bidp = struct.unpack('>qii', chunk[:16])
            
            # Preise in Float umwandeln
            ask = askp / 100000
            bid = bidp / 100000
            
            # Zeitstempel in datetime umwandeln
            dt = datetime.fromtimestamp(timestamp / 1000)
            
            data.append([dt, ask, bid])
            
        return pd.DataFrame(data, columns=['datetime', 'ask', 'bid'])
    except Exception as e:
        print(f"Error downloading data for {date}: {str(e)}")
        return None

def download_month_data(pair, year, month):
    """Download data for an entire month"""
    print(f"Downloading {pair} data for {year}-{month}")
    
    all_data = []
    _, days_in_month = monthrange(year, month)
    
    for day in range(1, days_in_month + 1):
        for hour in range(24):
            df = download_tick(pair, year, month, day, hour)
            if df is not None and not df.empty:
                # Nur den letzten Tick der Stunde nehmen für OHLC
                hourly_data = df.set_index('datetime').last('1H')
                all_data.append(hourly_data)
            
            # Kurze Pause um den Server nicht zu überlasten
            time.sleep(0.1)
    
    if all_data:
        monthly_df = pd.concat(all_data)
        monthly_df.sort_index(inplace=True)
        return monthly_df
    return None

def download_parallel(pair="EURUSD", start_date=datetime(2023, 1, 1), end_date=datetime(2024, 1, 1)):
    """Download data in parallel for each month"""
    print(f"Starting parallel download for {pair} from {start_date} to {end_date}")
    
    # Liste der Monate erstellen, die heruntergeladen werden sollen
    months_to_download = []
    current_date = start_date
    while current_date < end_date:
        months_to_download.append((current_date.year, current_date.month))
        # Zum nächsten Monat
        if current_date.month == 12:
            current_date = datetime(current_date.year + 1, 1, 1)
        else:
            current_date = datetime(current_date.year, current_date.month + 1, 1)
    
    # Paralleles Herunterladen mit ThreadPoolExecutor
    monthly_data = {}
    with ThreadPoolExecutor(max_workers=12) as executor:
        # Erstelle Future-Objekte für jeden Monat
        future_to_month = {
            executor.submit(download_month_data, pair, year, month): (year, month)
            for year, month in months_to_download
        }
        
        # Verarbeite die Ergebnisse, sobald sie fertig sind
        for future in as_completed(future_to_month):
            year, month = future_to_month[future]
            try:
                monthly_df = future.result()
                if monthly_df is not None:
                    monthly_data[(year, month)] = monthly_df
                    print(f"Successfully downloaded data for {year}-{month}")
            except Exception as e:
                print(f"Error downloading data for {year}-{month}: {str(e)}")
    
    if monthly_data:
        # Alle Monatsdaten zusammenführen
        final_df = pd.concat(monthly_data.values())
        final_df.sort_index(inplace=True)
        
        # Spalten umbenennen und OHLC Format erstellen
        final_df.columns = ["Close", "Open"]
        final_df['High'] = final_df['Close'].rolling(window=1).max()
        final_df['Low'] = final_df['Close'].rolling(window=1).min()
        
        # Als CSV speichern
        output_file = os.path.join("Example_HisData", f"{pair}_1H_2023.csv")
        final_df.to_csv(output_file)
        print(f"\nData successfully saved to {output_file}")
        print(f"Downloaded {len(final_df)} hourly records")
    else:
        print("No data was downloaded")

if __name__ == "__main__":
    # Verzeichnis erstellen falls es nicht existiert
    os.makedirs("Example_HisData", exist_ok=True)
    
    # EURUSD Daten für 2023 parallel herunterladen
    download_parallel()
