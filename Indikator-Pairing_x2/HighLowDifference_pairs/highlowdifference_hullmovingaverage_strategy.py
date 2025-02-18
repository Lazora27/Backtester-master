import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'HullMovingAverage': 1.0
        })
    )
