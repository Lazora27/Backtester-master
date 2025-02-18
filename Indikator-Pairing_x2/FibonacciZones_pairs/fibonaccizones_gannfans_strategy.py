import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und GannFans
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'GannFans': 1.0
        })
    )
