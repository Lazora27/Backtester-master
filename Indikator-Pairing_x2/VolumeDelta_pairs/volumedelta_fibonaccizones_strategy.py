import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'FibonacciZones': 1.0
        })
    )
