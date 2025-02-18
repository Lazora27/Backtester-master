import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'FibonacciZones': 1.0
        })
    )
