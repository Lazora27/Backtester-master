import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_TrendExhaustion_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und TrendExhaustion
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'TrendExhaustion': {
                'class': TrendExhaustion,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendExhaustion'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'TrendExhaustion': 1.0
        })
    )
