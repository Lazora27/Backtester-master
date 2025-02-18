import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RainbowMovingAverage_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RainbowMovingAverage und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'RainbowMovingAverage': 1.0,
            'WeeklyCycle': 1.0
        })
    )
