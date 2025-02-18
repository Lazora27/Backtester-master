import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'ParabolicSAR': 1.0
        })
    )
