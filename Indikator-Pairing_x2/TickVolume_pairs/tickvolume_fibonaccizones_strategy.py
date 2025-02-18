import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'FibonacciZones': 1.0
        })
    )
