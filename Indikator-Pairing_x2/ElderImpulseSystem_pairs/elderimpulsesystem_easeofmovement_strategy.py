import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'EaseOfMovement': 1.0
        })
    )
