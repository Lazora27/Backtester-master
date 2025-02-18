import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_AutoFibonacci_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und AutoFibonacci
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'AutoFibonacci': 1.0
        })
    )
