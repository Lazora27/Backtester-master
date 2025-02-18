import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FibonacciZones_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FibonacciZones und MassIndex
    """
    
    params = (
        ('indicators', {
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'FibonacciZones': 1.0,
            'MassIndex': 1.0
        })
    )
