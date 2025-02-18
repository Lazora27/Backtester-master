import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
