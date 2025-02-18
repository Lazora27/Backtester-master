import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverageCycleDetector_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverageCycleDetector und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'MovingAverageCycleDetector': {
                'class': MovingAverageCycleDetector,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageCycleDetector'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'MovingAverageCycleDetector': 1.0,
            'SmoothedCycle': 1.0
        })
    )
