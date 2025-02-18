import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'SmoothedCycle': 1.0
        })
    )
