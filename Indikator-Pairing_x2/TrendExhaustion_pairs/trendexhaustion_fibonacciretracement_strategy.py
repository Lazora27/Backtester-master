import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrendExhaustion_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrendExhaustion und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'TrendExhaustion': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
