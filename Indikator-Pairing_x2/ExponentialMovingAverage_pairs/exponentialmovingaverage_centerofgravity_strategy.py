import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'CenterOfGravity': 1.0
        })
    )
