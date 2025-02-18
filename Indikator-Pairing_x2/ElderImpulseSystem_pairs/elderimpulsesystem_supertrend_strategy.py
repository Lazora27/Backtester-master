import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und SuperTrend
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'SuperTrend': 1.0
        })
    )
