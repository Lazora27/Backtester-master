import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
