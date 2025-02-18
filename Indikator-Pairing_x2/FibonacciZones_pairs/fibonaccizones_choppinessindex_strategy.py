import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
