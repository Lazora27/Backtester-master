import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und GannAngles
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'GannAngles': 1.0
        })
    )
