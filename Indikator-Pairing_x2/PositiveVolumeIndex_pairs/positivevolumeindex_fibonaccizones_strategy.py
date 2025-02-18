import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'FibonacciZones': 1.0
        })
    )
