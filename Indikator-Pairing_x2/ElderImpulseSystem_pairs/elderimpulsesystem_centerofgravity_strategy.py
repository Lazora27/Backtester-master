import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'CenterOfGravity': 1.0
        })
    )
