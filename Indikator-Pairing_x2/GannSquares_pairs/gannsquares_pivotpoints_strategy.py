import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_PivotPoints_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und PivotPoints
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'PivotPoints': 1.0
        })
    )
