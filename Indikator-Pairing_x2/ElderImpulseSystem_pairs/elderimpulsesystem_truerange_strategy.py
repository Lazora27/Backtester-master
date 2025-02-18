import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und TrueRange
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'TrueRange': 1.0
        })
    )
