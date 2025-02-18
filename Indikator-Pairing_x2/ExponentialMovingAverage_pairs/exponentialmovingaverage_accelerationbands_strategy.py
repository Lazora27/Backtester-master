import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'AccelerationBands': 1.0
        })
    )
