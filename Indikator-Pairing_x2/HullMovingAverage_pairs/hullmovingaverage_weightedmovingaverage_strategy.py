import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
