import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
