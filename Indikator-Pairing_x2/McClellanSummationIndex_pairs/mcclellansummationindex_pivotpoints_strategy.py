import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und PivotPoints
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'PivotPoints': 1.0
        })
    )
