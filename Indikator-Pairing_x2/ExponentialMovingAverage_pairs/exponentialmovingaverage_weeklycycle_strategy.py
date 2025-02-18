import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ExponentialMovingAverage_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ExponentialMovingAverage und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'ExponentialMovingAverage': 1.0,
            'WeeklyCycle': 1.0
        })
    )
