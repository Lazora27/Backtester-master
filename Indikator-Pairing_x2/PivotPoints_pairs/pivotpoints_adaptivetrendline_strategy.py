import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
