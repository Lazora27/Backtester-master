import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_AdaptiveTrendLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und AdaptiveTrendLine
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'AdaptiveTrendLine': 1.0
        })
    )
