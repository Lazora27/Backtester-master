import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_MovingAverageCycleDetector_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und MovingAverageCycleDetector
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'MovingAverageCycleDetector': {
                'class': MovingAverageCycleDetector,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageCycleDetector'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'MovingAverageCycleDetector': 1.0
        })
    )
