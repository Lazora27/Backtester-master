import backtrader as bt
from .base_strategy import FlexibleStrategy
from Indikatoren.Momentum_Indikatoren.TrendExhaustion.trend_exhaustion import TrendExhaustion

class CombinedStrategy(FlexibleStrategy):
    """
    Beispiel einer kombinierten Strategie mit mehreren Indikatoren
    """
    
    params = (
        ('indicators', {
            'trend_exhaustion': {
                'class': TrendExhaustion,
                'params': {
                    'period': 14,
                    'volume_period': 10,
                    'momentum_period': 5
                }
            },
            'rsi': {
                'class': bt.indicators.RSI,
                'params': {
                    'period': 14
                }
            },
            'macd': {
                'class': bt.indicators.MACD,
                'params': {
                    'period_me1': 12,
                    'period_me2': 26,
                    'period_signal': 9
                }
            }
        }),
        ('weights', {
            'trend_exhaustion': 2.0,  # Höhere Gewichtung für Trend Exhaustion
            'rsi': 1.0,
            'macd': 1.0
        })
    )
