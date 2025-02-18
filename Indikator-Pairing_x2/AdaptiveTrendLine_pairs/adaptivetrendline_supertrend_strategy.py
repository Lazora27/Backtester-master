import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und SuperTrend
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'SuperTrend': 1.0
        })
    )
