import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverage_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverage und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'MovingAverage': 1.0,
            'WeeklyCycle': 1.0
        })
    )
