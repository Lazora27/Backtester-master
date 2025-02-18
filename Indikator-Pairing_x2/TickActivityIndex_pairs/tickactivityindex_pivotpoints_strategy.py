import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und PivotPoints
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'PivotPoints': 1.0
        })
    )
