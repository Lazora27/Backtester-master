import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und BollingerBands
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'BollingerBands': 1.0
        })
    )
