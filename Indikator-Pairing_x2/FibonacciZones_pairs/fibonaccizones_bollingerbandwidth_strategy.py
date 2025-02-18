import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
