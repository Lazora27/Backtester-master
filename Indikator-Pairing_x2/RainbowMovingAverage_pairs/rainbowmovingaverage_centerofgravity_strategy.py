import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'CenterOfGravity': 1.0
        })
    )
