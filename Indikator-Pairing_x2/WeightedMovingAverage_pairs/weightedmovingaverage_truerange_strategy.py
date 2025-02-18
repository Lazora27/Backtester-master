import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und TrueRange
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'TrueRange': 1.0
        })
    )
