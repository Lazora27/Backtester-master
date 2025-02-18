import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_MovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und MovingAverage
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'MovingAverage': {
                'class': MovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MovingAverage'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'MovingAverage': 1.0
        })
    )
