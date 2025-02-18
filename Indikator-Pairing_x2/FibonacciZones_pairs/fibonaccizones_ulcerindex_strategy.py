import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'UlcerIndex': 1.0
        })
    )
