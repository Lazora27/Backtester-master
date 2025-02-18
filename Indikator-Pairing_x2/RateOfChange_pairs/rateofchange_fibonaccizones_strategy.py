import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'FibonacciZones': 1.0
        })
    )
