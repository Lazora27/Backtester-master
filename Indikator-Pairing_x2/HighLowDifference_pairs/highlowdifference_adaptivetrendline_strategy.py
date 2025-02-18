import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
