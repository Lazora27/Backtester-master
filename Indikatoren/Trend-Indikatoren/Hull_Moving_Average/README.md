# Hull Moving Average (HMA)

Der Hull Moving Average ist ein fortgeschrittener gleitender Durchschnitt, der das Lag reduziert.

## Parameter
- period (Standard: 20): Die Anzahl der Perioden für die Berechnung

## Verwendung
```python
from HMA.hma import HullMovingAverage

# In Ihrer Strategie
hma = HullMovingAverage(self.data, period=20)
```

## Beschreibung
Der HMA wurde von Alan Hull entwickelt und kombiniert mehrere WMAs unterschiedlicher Perioden, um das Lag zu reduzieren. Die Formel lautet:
HMA = WMA(2*WMA(n/2) - WMA(n)), sqrt(n))

Der HMA reagiert schneller auf Preisänderungen als traditionelle Moving Averages, während er gleichzeitig weniger Rauschen erzeugt.
