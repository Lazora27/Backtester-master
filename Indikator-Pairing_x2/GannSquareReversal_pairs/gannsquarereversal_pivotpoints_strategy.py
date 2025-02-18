import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und PivotPoints
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'PivotPoints': 1.0
        })
    )
