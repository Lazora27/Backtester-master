import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und MovingAverage
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'MovingAverage': 1.0
        })
    )
