import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und SuperTrend
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'SuperTrend': 1.0
        })
    )
