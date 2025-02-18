import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
