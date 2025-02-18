import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
