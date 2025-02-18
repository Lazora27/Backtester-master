import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciExtensions_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciExtensions und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'FibonacciExtensions': 1.0,
            'CenterOfGravity': 1.0
        })
    )
