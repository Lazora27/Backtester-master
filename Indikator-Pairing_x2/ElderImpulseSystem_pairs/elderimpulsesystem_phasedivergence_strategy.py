import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'PhaseDivergence': 1.0
        })
    )
