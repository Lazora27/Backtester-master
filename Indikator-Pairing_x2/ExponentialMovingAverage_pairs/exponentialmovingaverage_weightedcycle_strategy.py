import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'WeightedCycle': 1.0
        })
    )
