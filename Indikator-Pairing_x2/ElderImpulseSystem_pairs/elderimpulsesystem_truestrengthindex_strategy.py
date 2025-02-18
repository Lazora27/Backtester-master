import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_TrueStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und TrueStrengthIndex
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'TrueStrengthIndex': 1.0
        })
    )
