import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
