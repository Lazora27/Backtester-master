import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und PivotPoints
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'PivotPoints': 1.0
        })
    )
