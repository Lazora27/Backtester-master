import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und TimeCycle
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'TimeCycle': 1.0
        })
    )
