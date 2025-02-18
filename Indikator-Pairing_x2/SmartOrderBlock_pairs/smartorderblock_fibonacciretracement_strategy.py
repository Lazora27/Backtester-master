import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
