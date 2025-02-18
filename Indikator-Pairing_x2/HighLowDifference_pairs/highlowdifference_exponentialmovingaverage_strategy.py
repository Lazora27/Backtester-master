import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
