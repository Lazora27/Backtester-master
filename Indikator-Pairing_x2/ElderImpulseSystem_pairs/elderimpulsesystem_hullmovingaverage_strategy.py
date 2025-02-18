import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'HullMovingAverage': 1.0
        })
    )
