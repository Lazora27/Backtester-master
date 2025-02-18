import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_ElderImpulseSystem_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und ElderImpulseSystem
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'ElderImpulseSystem': 1.0
        })
    )
