# Moving Average (MA)

Ein einfacher Moving Average (Gleitender Durchschnitt) Indikator.

## Parameter
- period (Standard: 20): Die Anzahl der Perioden für die Berechnung

## Verwendung
```python
from MA.ma import MovingAverage

# In Ihrer Strategie
ma = MovingAverage(self.data, period=20)
```

## Beschreibung
Der Moving Average berechnet den Durchschnitt der letzten N Perioden. Er ist der einfachste und am häufigsten verwendete Trendindikator.
