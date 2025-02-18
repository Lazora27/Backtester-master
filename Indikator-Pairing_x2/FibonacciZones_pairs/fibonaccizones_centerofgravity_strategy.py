import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'CenterOfGravity': 1.0
        })
    )
