import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
