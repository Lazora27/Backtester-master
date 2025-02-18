import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und GannAngles
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'GannAngles': 1.0
        })
    )
