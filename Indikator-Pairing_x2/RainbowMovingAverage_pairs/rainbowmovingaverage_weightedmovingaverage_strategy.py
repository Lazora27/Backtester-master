import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
