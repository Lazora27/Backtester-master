import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'BollingerPercentB': 1.0
        })
    )
