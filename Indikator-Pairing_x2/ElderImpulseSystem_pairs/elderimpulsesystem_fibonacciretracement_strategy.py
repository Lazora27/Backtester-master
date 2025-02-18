import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_FibonacciRetracement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und FibonacciRetracement
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'FibonacciRetracement': {
                'class': FibonacciRetracement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FibonacciRetracement'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'FibonacciRetracement': 1.0
        })
    )
