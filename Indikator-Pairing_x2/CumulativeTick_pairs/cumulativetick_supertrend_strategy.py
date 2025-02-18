import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und SuperTrend
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'SuperTrend': 1.0
        })
    )
