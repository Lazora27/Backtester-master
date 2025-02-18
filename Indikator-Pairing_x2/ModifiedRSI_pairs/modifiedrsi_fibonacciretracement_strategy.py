import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
