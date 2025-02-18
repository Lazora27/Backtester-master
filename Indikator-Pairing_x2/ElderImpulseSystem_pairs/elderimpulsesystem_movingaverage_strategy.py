import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und MovingAverage
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'MovingAverage': 1.0
        })
    )
