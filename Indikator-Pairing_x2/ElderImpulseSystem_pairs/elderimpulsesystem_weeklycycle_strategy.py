import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'WeeklyCycle': 1.0
        })
    )
