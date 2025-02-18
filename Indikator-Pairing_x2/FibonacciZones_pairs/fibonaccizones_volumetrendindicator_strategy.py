import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
