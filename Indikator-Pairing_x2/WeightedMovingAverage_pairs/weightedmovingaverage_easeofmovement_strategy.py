import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'EaseOfMovement': 1.0
        })
    )
