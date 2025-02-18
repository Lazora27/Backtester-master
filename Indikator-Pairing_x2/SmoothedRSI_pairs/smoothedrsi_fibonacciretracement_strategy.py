import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
