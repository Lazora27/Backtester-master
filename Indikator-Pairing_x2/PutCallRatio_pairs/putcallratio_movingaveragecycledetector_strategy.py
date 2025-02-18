import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_MovingAverageCycleDetector_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und MovingAverageCycleDetector
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'MovingAverageCycleDetector': {
                'class': MovingAverageCycleDetector,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageCycleDetector'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'MovingAverageCycleDetector': 1.0
        })
    )
