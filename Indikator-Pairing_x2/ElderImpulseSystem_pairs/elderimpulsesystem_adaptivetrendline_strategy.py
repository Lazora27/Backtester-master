import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
