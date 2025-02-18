import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
