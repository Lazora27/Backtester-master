import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'AdaptiveATR': 1.0
        })
    )
