import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_FibonacciExtensions_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und FibonacciExtensions
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'FibonacciExtensions': {
                'class': FibonacciExtensions,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciExtensions'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'FibonacciExtensions': 1.0
        })
    )
