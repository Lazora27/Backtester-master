import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
