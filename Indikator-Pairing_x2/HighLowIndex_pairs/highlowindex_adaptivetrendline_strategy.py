import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
