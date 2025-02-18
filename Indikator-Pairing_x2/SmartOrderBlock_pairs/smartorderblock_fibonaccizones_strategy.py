import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmartOrderBlock_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmartOrderBlock und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'SmartOrderBlock': {
                'class': SmartOrderBlock,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmartOrderBlock'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'SmartOrderBlock': 1.0,
            'FibonacciZones': 1.0
        })
    )
