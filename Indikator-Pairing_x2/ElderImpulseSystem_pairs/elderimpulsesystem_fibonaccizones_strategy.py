import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_FibonacciZones_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und FibonacciZones
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'FibonacciZones': {
                'class': FibonacciZones,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciZones'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'FibonacciZones': 1.0
        })
    )
