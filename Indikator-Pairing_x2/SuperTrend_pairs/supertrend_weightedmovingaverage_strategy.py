import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
