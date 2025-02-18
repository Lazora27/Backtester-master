import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
