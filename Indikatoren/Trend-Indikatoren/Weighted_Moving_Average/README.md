# Weighted Moving Average (WMA)

Der Weighted Moving Average ist ein gleitender Durchschnitt, der die Werte linear gewichtet.

## Parameter
- period (Standard: 20): Die Anzahl der Perioden für die Berechnung

## Verwendung
```python
from WMA.wma import WeightedMovingAverage

# In Ihrer Strategie
wma = WeightedMovingAverage(self.data, period=20)
```

## Beschreibung
Der WMA gewichtet die Preise linear, wobei der neueste Preis das höchste Gewicht erhält. Dies macht ihn reaktiver als den SMA, aber weniger volatil als den EMA.
