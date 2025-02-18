import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'WeightedCycle': 1.0
        })
    )
