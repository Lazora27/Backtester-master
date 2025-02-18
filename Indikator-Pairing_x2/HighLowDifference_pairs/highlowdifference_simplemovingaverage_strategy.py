import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_SimpleMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und SimpleMovingAverage
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'SimpleMovingAverage': {
                'class': SimpleMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SimpleMovingAverage'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'SimpleMovingAverage': 1.0
        })
    )
