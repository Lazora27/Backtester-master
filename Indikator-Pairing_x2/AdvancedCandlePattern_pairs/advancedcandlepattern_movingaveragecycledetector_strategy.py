import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_MovingAverageCycleDetector_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und MovingAverageCycleDetector
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'MovingAverageCycleDetector': {
                'class': MovingAverageCycleDetector,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverageCycleDetector'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'MovingAverageCycleDetector': 1.0
        })
    )
