import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'FibonacciZones': 1.0
        })
    )
