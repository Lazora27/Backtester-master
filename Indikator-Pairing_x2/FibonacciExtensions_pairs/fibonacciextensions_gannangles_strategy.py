import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und GannAngles
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'GannAngles': 1.0
        })
    )
