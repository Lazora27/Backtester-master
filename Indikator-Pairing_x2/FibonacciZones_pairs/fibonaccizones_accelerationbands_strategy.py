import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'AccelerationBands': 1.0
        })
    )
