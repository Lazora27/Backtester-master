import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
