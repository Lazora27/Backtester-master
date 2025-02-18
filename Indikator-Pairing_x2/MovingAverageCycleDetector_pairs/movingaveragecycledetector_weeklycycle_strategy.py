import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverageCycleDetector_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverageCycleDetector und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'MovingAverageCycleDetector': {
                'class': MovingAverageCycleDetector,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageCycleDetector'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'MovingAverageCycleDetector': 1.0,
            'WeeklyCycle': 1.0
        })
    )
