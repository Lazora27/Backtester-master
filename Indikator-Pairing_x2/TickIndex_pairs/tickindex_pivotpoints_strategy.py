import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und PivotPoints
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'PivotPoints': 1.0
        })
    )
