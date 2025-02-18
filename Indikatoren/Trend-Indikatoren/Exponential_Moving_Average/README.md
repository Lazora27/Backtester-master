# Exponential Moving Average (EMA)

Der Exponential Moving Average ist ein gleitender Durchschnitt, der neueren Daten ein höheres Gewicht gibt.

## Parameter
- period (Standard: 20): Die Anzahl der Perioden für die Berechnung

## Verwendung
```python
from EMA.ema import ExponentialMovingAverage

# In Ihrer Strategie
ema = ExponentialMovingAverage(self.data, period=20)
```

## Beschreibung
Der EMA reagiert schneller auf Preisänderungen als der einfache Moving Average, da er neuere Daten stärker gewichtet. Dies macht ihn besonders nützlich in Trending-Märkten.
