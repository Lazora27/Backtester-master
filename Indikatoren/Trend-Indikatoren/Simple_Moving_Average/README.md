# Simple Moving Average (SMA)

Der Simple Moving Average ist der klassische gleitende Durchschnitt mit gleichmäßiger Gewichtung aller Werte.

## Parameter
- period (Standard: 20): Die Anzahl der Perioden für die Berechnung

## Verwendung
```python
from SMA.sma import SimpleMovingAverage

# In Ihrer Strategie
sma = SimpleMovingAverage(self.data, period=20)
```

## Beschreibung
Der SMA ist der am häufigsten verwendete Moving Average. Er gewichtet alle Preise im Berechnungszeitraum gleich und ist besonders gut geeignet, um den allgemeinen Trend zu identifizieren.
