import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'IchimokuCloud': 1.0
        })
    )
