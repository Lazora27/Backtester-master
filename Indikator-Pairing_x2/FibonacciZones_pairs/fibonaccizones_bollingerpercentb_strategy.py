import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'BollingerPercentB': 1.0
        })
    )
