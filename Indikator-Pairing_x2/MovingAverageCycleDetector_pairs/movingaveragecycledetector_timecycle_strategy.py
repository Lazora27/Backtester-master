import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MovingAverageCycleDetector_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MovingAverageCycleDetector und TimeCycle
    """
    
    params = (
        ('indicators', {
            'MovingAverageCycleDetector': {
                'class': MovingAverageCycleDetector,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageCycleDetector'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'MovingAverageCycleDetector': 1.0,
            'TimeCycle': 1.0
        })
    )
