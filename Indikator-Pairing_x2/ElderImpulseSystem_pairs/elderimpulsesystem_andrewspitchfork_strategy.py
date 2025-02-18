import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
