import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciRetracement_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciRetracement und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'FibonacciRetracement': 1.0,
            'CenterOfGravity': 1.0
        })
    )
