import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
