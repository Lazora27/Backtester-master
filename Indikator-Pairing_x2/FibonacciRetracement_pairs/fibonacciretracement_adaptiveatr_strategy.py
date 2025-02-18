import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'AdaptiveATR': 1.0
        })
    )
