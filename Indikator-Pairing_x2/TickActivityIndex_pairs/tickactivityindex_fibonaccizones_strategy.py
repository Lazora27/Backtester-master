import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'FibonacciZones': 1.0
        })
    )
