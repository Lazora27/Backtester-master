import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'AverageLogRange': 1.0
        })
    )
