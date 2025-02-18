import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'WeightedCycle': 1.0
        })
    )
