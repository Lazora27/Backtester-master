import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'CumulativeTick': 1.0
        })
    )
