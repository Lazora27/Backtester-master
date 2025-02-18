import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
