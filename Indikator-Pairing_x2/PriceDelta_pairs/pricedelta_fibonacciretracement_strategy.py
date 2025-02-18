import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
