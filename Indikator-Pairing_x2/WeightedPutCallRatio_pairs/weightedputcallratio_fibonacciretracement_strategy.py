import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedPutCallRatio_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedPutCallRatio und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'WeightedPutCallRatio': {
                'class': WeightedPutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedPutCallRatio'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'WeightedPutCallRatio': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
