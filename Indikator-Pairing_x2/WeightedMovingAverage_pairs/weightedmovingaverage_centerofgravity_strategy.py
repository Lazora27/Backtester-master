import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WeightedMovingAverage_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WeightedMovingAverage und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'WeightedMovingAverage': 1.0,
            'CenterOfGravity': 1.0
        })
    )
