import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
