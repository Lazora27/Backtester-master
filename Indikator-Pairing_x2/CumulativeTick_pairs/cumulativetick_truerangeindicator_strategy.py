import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_TrueRangeIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und TrueRangeIndicator
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'TrueRangeIndicator': {
                'class': TrueRangeIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRangeIndicator'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'TrueRangeIndicator': 1.0
        })
    )
