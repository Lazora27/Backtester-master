import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowDifference_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowDifference und PivotPoints
    """
    
    params = (
        ('indicators', {
            'HighLowDifference': {
                'class': HighLowDifference,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowDifference'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'HighLowDifference': 1.0,
            'PivotPoints': 1.0
        })
    )
