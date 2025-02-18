import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und VWAPBands
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'VWAPBands': 1.0
        })
    )
