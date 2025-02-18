import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'BollingerPercentB': 1.0
        })
    )
