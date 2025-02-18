import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
